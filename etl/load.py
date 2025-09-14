# etl/load.py
import sqlite3
import pandas as pd
import os # Import os for directory creation

def load_data(df):
    """Loads the transformed data into an SQLite database."""
    if df is None or df.empty:
        print("❌ No data to load.")
        return
        
    # Ensure the database directory exists
    db_dir = 'database'
    os.makedirs(db_dir, exist_ok=True) # Create 'database' directory if it doesn't exist

    db_path = os.path.join(db_dir, 'sales.db')
    
    # Connect to the database
    conn = None # Initialize conn to None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Create a table (if it doesn't exist) with appropriate schema
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY,
            date TEXT,
            product TEXT,
            quantity INTEGER,
            price REAL,        -- Price is now standardized in INR
            currency TEXT,     -- Will now always be 'INR' after transformation
            region TEXT,
            total_sales_amount REAL
        );
        """
        cursor.execute(create_table_sql)
        
        # Load data into the table
        # 'if_exists='replace'' will overwrite the table if it exists.
        # For appending, use 'append'.
        df.to_sql('sales', conn, if_exists='replace', index=False)
        
        print("✅ Data loading complete. Check sales.db.")

    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    # This block runs only when load.py is executed directly for testing
    print("--- Running load.py directly for testing ---")
    # Create a sample DataFrame that mimics transformed data for testing
    sample_df_for_load = pd.DataFrame({
        'id': [1], 
        'date': ['2025-08-01'], 
        'product': ['Laptop'], 
        'quantity': [2], 
        'price': [55000.0], 
        'currency': ['INR'], 
        'region': ['India'], 
        'total_sales_amount': [110000.0]
    })
    load_data(sample_df_for_load)
    print("---------------------------------------------")
