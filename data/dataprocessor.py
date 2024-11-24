import pandas as pd
import numpy as np

def process_fabric_file(file_path):
    """
    Process fabric data from CSV or Excel file into a dictionary where column names are keys
    and all values in that column become a list.
    
    Parameters:
    file_path (str): Path to the CSV or Excel file
    
    Returns:
    dict: Dictionary with column names as keys and column values as lists
    """
    try:
        # Read the file based on its extension
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(file_path)
        else:
            raise ValueError("File must be either CSV or Excel format")
        
        # Create the fabric dictionary
        fabric = {}
        
        # Process each column
        for column in df.columns:
            # Convert column to list, removing any NaN values
            values = df[column].dropna().tolist()
            # Clean the values (remove leading/trailing spaces and convert to string if needed)
            values = [str(val).strip() if not pd.isna(val) else val for val in values]
            # Add to dictionary
            fabric[column] = values
        
        return fabric

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        return None
    except Exception as e:
        print(f"Error processing file: {e}")
        return None

def print_fabric_dict(fabric):
    """
    Print the fabric dictionary in a formatted way
    """
    if fabric is None:
        return
    
    print("fabric = {")
    for key, values in fabric.items():
        print(f"    '{key}': [")
        # Print first few and last few items with ellipsis in between if list is long
        if len(values) > 10:
            # Print first 5 items
            for item in values[:5]:
                print(f"        '{item}',")
            print("        ...")
            # Print last 5 items
            for item in values[-5:]:
                print(f"        '{item}',")
        else:
            # Print all items if list is short
            for item in values:
                print(f"        '{item}',")
        print("    ],")
    print("}")

# Example usage
if __name__ == "__main__":
    # Example with sample file paths
    file_paths = [
        "data\CompleteData.xlsx",  # For CSV file
         # For Excel file
    ]
    
    for file_path in file_paths:
        print(f"\nProcessing {file_path}...")
        fabric = process_fabric_file(file_path)
        if fabric:
            print_fabric_dict(fabric)
            
            # Print some statistics
            print("\nData Statistics:")
            print("-" * 50)
            for column, values in fabric.items():
                print(f"{column}: {len(values)} items")

# Example of expected data structure:
"""
fabric = {
    'Cost': [
        'Moderate',
        'High',
        'Low to Moderate',
        ...
    ],
    'Resistance': [
        'High (Durable)',
        'Moderate',
        'Moderate',
        ...
    ],
    ...
}
"""

# Additional utility functions for data validation and cleaning
def validate_fabric_data(fabric):
    """
    Validate the fabric dictionary structure and data
    """
    if not isinstance(fabric, dict):
        return False, "Data must be in dictionary format"
    
    for key, values in fabric.items():
        if not isinstance(values, list):
            return False, f"Values for key '{key}' must be in list format"
        if not all(isinstance(x, (str, int, float)) for x in values):
            return False, f"All values in '{key}' must be string or numeric"
    
    return True, "Data validation successful"

def save_fabric_data(fabric, output_file):
    """
    Save the fabric dictionary back to CSV or Excel
    """
    try:
        df = pd.DataFrame(fabric)
        if output_file.endswith('.csv'):
            df.to_csv(output_file, index=False)
        elif output_file.endswith(('.xlsx', '.xls')):
            df.to_excel(output_file, index=False)
        return True
    except Exception as e:
        print(f"Error saving data: {e}")
        return False