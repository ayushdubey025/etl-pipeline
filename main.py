from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

def run_etl_pipeline():
    """Orchestrates the entire ETL process."""
    print("🎬 Starting ETL pipeline...")
    
    # Step 1: Extract (Get the raw data)
    raw_data = extract_data()
    
    # Step 2: Transform (Process the extracted data)
    if raw_data is not None:
        transformed_data = transform_data(raw_daAta)
    else:
        transformed_data = None # Handle case where extraction failed
     
    # Step 3: Load (Store the transformed data)
    if transformed_data is not None: # Only load if transformation was successful
        load_data(transformed_data)
    else:
        print("Skipping data loading due to failed transformation.")
        
    print("✅ ETL pipeline finished.")

if __name__ == '__main__':
    # This block runs only when main.py is executed directly
    run_etl_pipeline()
