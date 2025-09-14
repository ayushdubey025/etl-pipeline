import pandas as pd
import os

def extract_data():
    try:
        # for combine path use os.path.join
        csv_path = os.path.join('data','sales_data.csv')
        json_path = os.path.join('data','sales_data.json')

        # EXTRACT FROM CSV
        csv_df = pd.read_csv(csv_path)

        
        # EXTRACT FROM JSON
        json_df = pd.read_json(json_path)

        # combine csv and json file
        combine_df = pd.concat([csv_df,json_df], ignore_index=True)
        print("✅ Data extraction complete.")
        return combine_df
    
    except Exception as e:
        print(f"Error  occurred: {e}")
        return None
    
if __name__ == '__main__':
    # This block runs only when extract.py is executed directly for testing
    print("--- Running extract.py directly for testing ---")
    extracted_df = extract_data()
    if extracted_df is not None:
        print("\nExtracted Data Sample (first 5 rows):")
        print(extracted_df.head())
    print("---------------------------------------------")