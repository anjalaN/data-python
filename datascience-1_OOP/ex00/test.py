#!/usr/bin/env python3
# def load_csv(life_expectancy_years.csv):
#     data = []
#     col = []
#     checkcol = False
#     print(load_csv)

import pandas as pd

# Example Series
years = pd.Series(['1800', '1801', '1802', '1803'])

print("Original data type:")
print(years)
print(years.dtypes)  # Check data type

# Convert to integers
years = years.astype(int)

print("\nConverted to integers:")
print(years)
print(years.dtypes)  # Check data type again
