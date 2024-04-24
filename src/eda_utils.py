import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
def load_data(file_path):
    """Load data from a CSV file."""
    return pd.read_csv(file_path)

def basic_info(data):
    """Print basic information about the DataFrame."""
    print("Basic Information:")
    print(data.info())

def basic_desc(data):
    """Print basic information about the DataFrame."""
    print("Basic Description:")
    print(data.describe())

def calculate_summary_stats(data):
    """Calculate summary statistics for each numeric column."""
    print("Summary Statistics:")
    
    # Exclude non-numeric columns
    numeric_data = data.select_dtypes(include='number')
    
    # Reset index to exclude it from summary statistics
    numeric_data.reset_index(drop=True, inplace=True)
    
    # Calculate summary statistics
    summary_stats = numeric_data.describe()
    
    # Calculate median
    median = numeric_data.median()
    
    # Calculate standard deviation
    std = numeric_data.std()
    
    # Calculate skewness
    skew = numeric_data.skew()
    
    # Calculate kurtosis
    kurtosis = numeric_data.kurt()
    
    # Create a list of summary statistics with descriptions
    summary_stats_list = [
        ('count', 'Number of non-null observations', summary_stats.loc['count']),
        ('mean', 'Mean of the values', summary_stats.loc['mean']),
        ('median', 'Median (50th percentile) of the values', median),
        ('standard deviation', 'Standard deviation of the values', std),
        ('skewness', 'Skewness of the distribution', skew),
        ('kurtosis', 'Kurtosis of the distribution', kurtosis)
    ]
    
    # Display the list
    for stat, description, value in summary_stats_list:
        print(f"{description}:")
        print(value)
    return summary_stats_list
 # 1. Missing Values
def missing_values(data):
    missing_values = data.isnull().sum()
    print("Missing Values:")
    print(missing_values)
# Incorrect Entries (Negative Values)

def count_negative_values(data):
    # Convert non-numeric values to NaN
    data_numeric = data.apply(pd.to_numeric, errors='coerce')
    # Count negative values for each attribute
    negative_counts = (data_numeric < 0).sum()
    print("\nCount of Negative Values in each Attribute:")
    print(negative_counts)
def remove_negative_rows(df, columns):
    """Remove rows containing negative values in specified columns from a DataFrame."""
    # Copy the original DataFrame to avoid modifying it directly
    cleaned_df = df.copy()
    
    # Remove rows with negative values in specified columns
    for col in columns:
        cleaned_df = cleaned_df[cleaned_df[col] >= 0] 
    return cleaned_df 
def plot_time_series(cleaned_df):
    print("Plotting time series...")
    """Plot time series for specified columns."""
    # Check if 'Timestamp' column is present in the DataFrame
    if 'Timestamp' not in cleaned_df.columns:
        print("Error: 'Timestamp' column not found in the DataFrame.")
        return
    
    # Define columns to plot
    columns_to_plot = ['GHI', 'DNI', 'DHI']
    
    # Check if the columns exist in the DataFrame
    for col in columns_to_plot:
        if col not in cleaned_df.columns:
            print(f"Error: Column '{col}' not found in the DataFrame.")
            return
    
    # Convert 'Timestamp' column to datetime format
    cleaned_df['Timestamp'] = pd.to_datetime(cleaned_df['Timestamp'])

    # Set 'Timestamp' column as index
    cleaned_df.set_index('Timestamp', inplace=True)

    # Define colors
    colors = sns.color_palette("husl", len(columns_to_plot))

    # Plot time series
    plt.figure(figsize=(12, 6))
    for i, col in enumerate(columns_to_plot):  # Specify columns to plot
        sns.lineplot(data=cleaned_df, x=cleaned_df.index, y=col, label=col, color=colors[i], linewidth=2, alpha=0.8)
    plt.xlabel('Time', fontsize=12)
    plt.ylabel('Value', fontsize=12)
    plt.title('Time Series Analysis for GHI, DNI, DHI', fontsize=16)
    plt.legend(fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()


def correlation_analysis(data):
    print("Performing correlation analysis...")
    """Perform correlation analysis between solar radiation and temperature variables."""
    # Select relevant columns for correlation analysis
    relevant_columns = ['GHI', 'DNI', 'DHI']  # Remove 'TModA' and 'TModB'

    # Check if all relevant columns exist in the DataFrame
    missing_columns = [col for col in relevant_columns if col not in data.columns]
    if missing_columns:
        print(f"Error: Columns {missing_columns} not found in the DataFrame.")
        return

    relevant_data = data[relevant_columns]

    # Calculate correlation matrix
    correlation_matrix = relevant_data.corr()

    # Plot heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Correlation Heatmap for GHI, DNI, DHI')



def plot_boxplot_outliers(data):
    print("Plotting boxplot with outliers for solar radiation and temperature data...")
    """Plot boxplot with outliers for solar radiation and temperature data."""
    # Select relevant columns
    solar_columns = ['GHI', 'DNI', 'DHI']
    temp_columns = ['Tamb', 'TModA', 'TModB']
    
    # Create subplots for solar radiation and temperature
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))
    
    # Plot box plots for solar radiation
    sns.boxplot(data=data[solar_columns], ax=axes[0])
    axes[0].set_title('Solar Radiation (W/m²)')
    axes[0].set_ylabel('Radiation (W/m²)')
    
    # Plot box plots for temperature
    sns.boxplot(data=data[temp_columns], ax=axes[1])
    axes[1].set_title('Temperature (°C)')
    axes[1].set_ylabel('Temperature (°C)')
    
    # Adjust layout
    plt.tight_layout()

