#!/usr/bin/env python3
import matplotlib.pyplot as plt
from load_csv import load_csv

def plot_life_expectancy_comparison(file_path, country1, country2):
    """
    Plots the life expectancy over time for two countries.

    Parameters:
    file_path (str): The path to the dataset file.
    country1 (str): The first country to plot data for.
    country2 (str): The second country to plot data for.
    """
    # Load the dataset
    df = load_csv(file_path)

    if df is not None:
        # Filter data for the specified countries
        country1_data = df[df['country'] == country1]
        country2_data = df[df['country'] == country2]

        # Extract years and life expectancy values
        years = country1_data.columns[1:]
        life_expectancy_country1 = country1_data.iloc[0, 1:].astype(float)
        life_expectancy_country2 = country2_data.iloc[0, 1:].astype(float)

        # Convert years to integers
        years = years.astype(int)

        # Plot the data
        plt.plot(years, life_expectancy_country1, label=country1, marker='o')
        plt.plot(years, life_expectancy_country2, label=country2, marker='x')

        # Set chart title and labels
        plt.title(f'Life Expectancy: {country1} vs {country2}')
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')
        plt.legend()
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

        # Display the plot
        plt.tight_layout()
        plt.show()
    else:
        print("Failed to load the dataset.")

if __name__ == "__main__":
    file_path = "life_expectancy_years.csv"
    country1 = "France"  # Your campus country
    country2 = "Germany"  # Another country of your choice
    plot_life_expectancy_comparison(file_path, country1, country2)
