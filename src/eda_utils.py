import pandas as pd

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

def run_eda(file_path):
    # Load data
    data = load_data(file_path)
    
    # Print basic information
    basic_info(data)
    basic_desc(data)
    
    # Calculate summary statistics
    summary_stats = calculate_summary_stats(data)
    
    return summary_stats

if __name__ == "__main__":
    file_path = 'dataset/benin-malanville.csv'  # Provide the path to your dataset
    summary_stats = run_eda(file_path)
