#!/usr/bin/env python3
from load_csv import dataset_dimensions

def main():
    file_path = "life_expectancy_years.csv"
    dimensions = dataset_dimensions(file_path)
    if dimensions:
        print(f"The dimensions of the dataset are: {dimensions}")
    else:
        print("Failed to read the dataset.")

if __name__ == "__main__":
    main()
