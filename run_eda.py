import sys
import os
import pandas as pd
from src import eda_utils

def run_eda(file_path):
    # Load data
    data = eda_utils.load_data(file_path)
    eda_utils.basic_info(data)
    eda_utils.basic_desc(data)
    # Calculate summary statistics
    summary_stats = eda_utils.calculate_summary_stats(data)
    print(summary_stats)  # Print the summary statistics

if __name__ == "__main__":
    file_path = 'dataset/benin-malanville.csv'  # Provide the path to your dataset
    run_eda(file_path)
