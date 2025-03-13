#!/user/bin/env python3
import pandas as pd
from load_csv import load_csv
def load_dataset(file_path):
    """
    reads dataset from the given file pathe, load to a file, and return .

    Parameters:
    file_path(str): The path to the dataset file.

    Returns:
    tuple: The dimensions of the dataset (rows, coloumns). 
    """
    try:
        #Read the dataset
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: the file at '{file_path}' was not found")
        return df
    except pd.errors.EmptyDataError:
        print(f"Error: The file at '{file_path}' is empty")
        return None
    except pd.errors.ParserError:
        print(f"Error: The file at '{file_path}' could not be parsed.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

        
if __name__ == "__main":
    file_path = "population_total.csv"
    data= load_dataset(file_path)
    
    if data is not None:
        print(data.head())
    else:
        print("Failed to load the dataset.")