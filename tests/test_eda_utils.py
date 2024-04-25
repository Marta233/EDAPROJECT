from unittest.mock import patch
import pandas as pd
from src import eda_utils
from unittest.mock import patch
# Load data function tests
def test_load_data(tmp_path):
    # Create a sample DataFrame
    sample_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    
    # Save sample data to a CSV file
    csv_file = tmp_path / "test_data.csv"
    sample_data.to_csv(csv_file, index=False)
    
    # Load data from the CSV file using the load_data function
    loaded_data = eda_utils.load_data(csv_file)
    
    # Assert that loaded_data is a DataFrame
    assert isinstance(loaded_data, pd.DataFrame)
    
    # Assert that loaded_data is equal to sample_data
    pd.testing.assert_frame_equal(loaded_data, sample_data)

# Basic info function test
def test_basic_info(capsys):
    # Create a sample DataFrame
    sample_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    
    # Call the basic_info function with sample data
    eda_utils.basic_info(sample_data)
    
    # Capture the printed output
    captured = capsys.readouterr()
    
    # Assert that the printed output contains the expected information
    assert "Basic Information" in captured.out
    assert "DataFrame" in captured.out

def test_basic_desc(capsys):
    # Create a sample DataFrame
    sample_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    
    # Call the basic_desc function with sample data
    eda_utils.basic_desc(sample_data)
    
    # Capture the printed output
    captured = capsys.readouterr()
    
    # Assert that the printed output contains the expected information
    assert "Basic Description" in captured.out
    assert "A" in captured.out  # Check if column names are present in the output
    assert "B" in captured.out
    assert "count" in captured.out
    assert "mean" in captured.out
    assert "std" in captured.out
    assert "min" in captured.out
    assert "25%" in captured.out
    assert "50%" in captured.out
    assert "75%" in captured.out
    assert "max" in captured.out


# Calculate summary statistics function test
def test_calculate_summary_stats():
    # Create a sample DataFrame
    sample_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    
    # Call the calculate_summary_stats function with sample data
    summary_stats_list = eda_utils.calculate_summary_stats(sample_data)
    
    # Check if the function returns a list
    assert isinstance(summary_stats_list, list)
    
    # Check if the returned list contains the expected information
    assert len(summary_stats_list) == 6  # Ensure all expected statistics are calculated

# Missing values function test
def test_missing_values(capsys):
    # Create a sample DataFrame with missing values
    sample_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, None]})
    
    # Call the missing_values function with sample data
    eda_utils.missing_values(sample_data)
    
    # Capture the printed output
    captured = capsys.readouterr()
    
    # Assert that the printed output contains the expected information
    assert "Missing Values" in captured.out
    assert "B    1" in captured.out  # Expecting 1 missing value in column B

# Count negative values function test
def test_count_negative_values(capsys):
    # Create a sample DataFrame with negative values
    sample_data = pd.DataFrame({'A': [1, -2, 3], 'B': [-4, 5, 6]})
    
    # Call the count_negative_values function with sample data
    eda_utils.count_negative_values(sample_data)
    
    # Capture the printed output
    captured = capsys.readouterr()
    
    # Assert that the printed output contains the expected information
    assert "Count of Negative Values" in captured.out
    assert "A    1" in captured.out  # Expecting 1 negative value in column A
    assert "B    1" in captured.out  # Expecting 1 negative value in column B

# Remove negative rows function test
def test_remove_negative_rows():
    # Create a sample DataFrame with negative values
    sample_data = pd.DataFrame({'A': [1, -2, 3], 'B': [-4, 5, 6]})
    
    # Call the remove_negative_rows function with sample data
    cleaned_data = eda_utils.remove_negative_rows(sample_data, ['A', 'B'])
    
    # Assert that the returned data does not contain negative values
    assert (cleaned_data[['A', 'B']] >= 0).all().all()

# Plot time series function test (assuming the function only prints)
def test_plot_time_series(capsys):
    # Create a sample DataFrame
    sample_data = pd.DataFrame({'Timestamp': ['2022-01-01', '2022-01-02', '2022-01-03'],
                                'GHI': [10, 20, 30], 'DNI': [15, 25, 35], 'DHI': [5, 15, 25]})
    
    # Call the plot_time_series function with sample data
    eda_utils.plot_time_series(sample_data)
    
    # Capture the printed output
    captured = capsys.readouterr()
    
    # Assert that the printed output contains the expected information
    assert "Plotting time series" in captured.out

# Correlation analysis function test (assuming the function only prints)
def test_correlation_analysis(capsys):
    # Create a sample DataFrame
    sample_data = pd.DataFrame({'GHI': [10, 20, 30], 'DNI': [15, 25, 35], 'DHI': [5, 15, 25]})

    # Patch the matplotlib figure creation to avoid the Tkinter backend error
    with patch("matplotlib.pyplot.figure"):
        # Call the correlation_analysis function with sample data
        eda_utils.correlation_analysis(sample_data)

    # Assert that the function printed the correct message
    captured = capsys.readouterr()
    assert "Performing correlation analysis..." in captured.out
