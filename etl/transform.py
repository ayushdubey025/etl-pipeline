# etl/transform.py
import pandas as pd

def transform_data(df):
    """Cleans and transforms the sales data, including currency conversion to INR."""
    if df is None:
        print("❌ No data provided for transformation.")
        return None
    
    # 1. Handle missing values: Fill missing 'quantity' and 'price' with 0
    # Updated to avoid FutureWarning by reassigning instead of using inplace=True
    df['quantity'] = df['quantity'].fillna(0)
    df['price'] = df['price'].fillna(0)

    # 2. Fix data types: Ensure 'quantity' and 'price' are numeric
    # 'errors='coerce'' will turn non-numeric values into NaN, then fillna handles them.
    # Convert quantity to int and price to float for calculations.
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce').astype('int')
    df['price'] = pd.to_numeric(df['price'], errors='coerce').astype('float')

    # 3. Standardize date format to DD-MM-YYYY (Indian format)
    # Robustly handle mixed date formats by trying multiple common formats
    # and combining the results.
    
    # Start by attempting to parse the most common format (e.g., YYYY-MM-DD)
    parsed_dates = pd.to_datetime(df['date'], format='%Y-%m-%d', errors='coerce')
    
    # Try parsing MM-DD-YYYY (e.g., 08-02-2025) for any dates that failed above
    parsed_dates = parsed_dates.combine_first(
        pd.to_datetime(df['date'], format='%m-%d-%Y', errors='coerce')
    )

    # Try parsing YYYY/MM/DD (e.g., 2025/08/03) for any remaining failed dates
    parsed_dates = parsed_dates.combine_first(
        pd.to_datetime(df['date'], format='%Y/%m/%d', errors='coerce')
    )
    
    # Finally, format the successfully parsed datetime objects into the desired DD-MM-YYYY string.
    # Any dates that couldn't be parsed by any of the above formats will remain NaT and become NULL.
    df['date'] = parsed_dates.dt.strftime('%d-%m-%Y')
    
    # 4. Currency Conversion to INR
    # Define simple exchange rates. In a production environment, these would be fetched from an API.
    exchange_rates = {
        'INR': 1.0,  # Base currency
        'USD': 83.0, # Approximate rate: 1 USD = 83 INR
        'EUR': 90.0  # Approximate rate: 1 EUR = 90 INR
    }

    # Apply the conversion using a lambda function.
    # .get() with a default of 1.0 handles cases where a currency might not be in our rates.
    df['price_in_inr'] = df.apply(
        lambda row: row['price'] * exchange_rates.get(row['currency'], 1.0),
        axis=1 # Apply function row by row
    )
    
    # Update the original 'price' column with the converted INR values
    df['price'] = df['price_in_inr'] 
    # Set the 'currency' column to 'INR' for all rows after conversion
    df['currency'] = 'INR'           
    # Drop the temporary column used for calculation
    df.drop(columns=['price_in_inr'], inplace=True) 

    # 5. Create/Recalculate 'total_sales_amount' based on the now-standardized INR price
    df['total_sales_amount'] = df['quantity'] * df['price']
    
    print("✅ Data transformation complete, including currency conversion to INR and date format.")
    return df

if __name__ == '__main__':
    # This block runs only when transform.py is executed directly for testing
    print("--- Running transform.py directly for testing ---")
    # Create a sample DataFrame that mimics the extracted data for testing
    sample_data_for_transform = {
        'id': [1, 5, 6, 8, 15, 3, 4], # Added IDs 3 and 4 to test your specific issue
        'date': ['2025-08-01', '2025-08-04', '08-05-2025', '2025/08/06', '2025-08-12', '08-02-2025', '2025/08/03'], # Added your problematic dates
        'product': ['Laptop', 'Mouse', 'Monitor', 'Laptop', 'Tablet', 'Headphones', 'Keyboard'],
        'quantity': [2, 7, 2, 1, 2, 10, 3],
        'price': [55000, None, 120, 750, None, 1500, 800], # Example of missing price from your data
        'currency': ['INR', 'INR', 'USD', 'EUR', 'USD', 'INR', 'INR'],
        'region': ['India', 'India', 'USA', 'Germany', 'USA', 'India', 'India']
    }
    sample_df = pd.DataFrame(sample_data_for_transform)
    
    print("\nOriginal Sample Data for Transformation:")
    print(sample_df)

    transformed_df = transform_data(sample_df.copy()) # Use .copy() to avoid SettingWithCopyWarning
    
    if transformed_df is not None:
        print("\nTransformed Sample Data (Prices in INR, Dates in DD-MM-YYYY):")
        print(transformed_df)
    print("---------------------------------------------")
