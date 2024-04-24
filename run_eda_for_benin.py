import sys
import os
import pandas as pd
from src import eda_utils
import matplotlib.pyplot as plt

def run_eda(file_path):
    # Load data
    data = eda_utils.load_data(file_path)
    eda_utils.basic_info(data)
    eda_utils.basic_desc(data)
    # Calculate summary statistics
    summary_stats = eda_utils.calculate_summary_stats(data)
    eda_utils.missing_values(data)
    eda_utils.count_negative_values(data)
    eda_utils.count_negative_values(data)
    # Remove rows with negative values in specific columns
    columns_to_check = ['GHI', 'DNI', 'DHI']
    cleaned_df = eda_utils.remove_negative_rows(data, columns_to_check)
    cleaned_df = cleaned_df.drop(columns=['Comments'])
    print("Cleaned data shape:", cleaned_df.shape)
    cleaned_df.info()
    eda_utils.plot_time_series(cleaned_df)
    eda_utils.correlation_analysis(cleaned_df)
    eda_utils.plot_boxplot_outliers(cleaned_df)
if __name__ == "__main__":
    file_path = 'dataset/benin-malanville.csv'  # Provide the path to your dataset
    run_eda(file_path)
    plt.show()  # Display all plots after running the analysis
