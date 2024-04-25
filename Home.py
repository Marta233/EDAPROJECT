import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
# Function to load data
@st.cache_data
def load_data(path: str):
    try:
        # Determine file type
        file_type = path.name.split('.')[-1]

        # Read the contents of the uploaded file
        if file_type == 'csv':
            # For CSV files
            return pd.read_csv(path)
        elif file_type == 'xlsx':
            # For XLSX files
            return pd.read_excel(path, engine='openpyxl')
        elif file_type == 'pdf':
            # For PDF files (if supported)
            st.error("PDF file format is not supported for direct loading.")
            return None
        else:
            st.error("Unsupported file format. Please upload a CSV, XLSX, or PDF file.")
            return None
    except Exception as e:
        st.error(f"An error occurred while loading the data: {str(e)}")
        return None
# Function to calculate summary statistics
def calculate_summary_stats(data, selected_column):
    """Calculate summary statistics for the selected column."""
    if selected_column == "Select a column":
        return
    if selected_column in data.columns:
        column_data = data[selected_column]
        if pd.api.types.is_numeric_dtype(column_data):
            # For numeric columns
            summary_stats = column_data.describe()
            # Calculate median, standard deviation, skewness, and kurtosis
            median = column_data.median()
            std = column_data.std()
            skew = column_data.skew()
            kurtosis = column_data.kurt()
            stats_data = {
                "Statistic": ["Count", "Mean", "Median", "Standard Deviation", "Skewness", "Kurtosis"],
                "Value": [summary_stats['count'], summary_stats['mean'], median, std, skew, kurtosis]
            }
            stats_df = pd.DataFrame(stats_data)
            st.write(stats_df)
        else:
            st.error("Unsupported column type. Please select a numerical column.")
    else:
        st.error(f"Column '{selected_column}' not found in the data.")
# Function to count negative values
def count_negative_values(data):
    """Count negative values for each column."""
    # Convert non-numeric values to NaN
    data_numeric = data.apply(pd.to_numeric, errors='coerce')
    # Count negative values for each column
    negative_counts = (data_numeric < 0).sum()
    return negative_counts
# Function to count missing values
def missing_values(data):
    """Count missing values for each column."""
    missing_values = data.isnull().sum()
    missing_percentage = (missing_values / len(data)) * 100
    missing_data = pd.DataFrame({'Missing Count': missing_values, 'Missing Percentage': missing_percentage})
    return missing_data
# Function to plot time series
def plot_time_series(cleaned_df):
    """Plot time series for specified columns."""
    # Check if 'Timestamp' column is present in the DataFrame
    if 'Timestamp' not in cleaned_df.columns:
        st.error("Error: 'Timestamp' column not found in the DataFrame.")
        return
    # Define columns to plot
    columns_to_plot = ['GHI', 'DNI', 'DHI']
    # Check if the columns exist in the DataFrame
    for col in columns_to_plot:
        if col not in cleaned_df.columns:
            st.error(f"Error: Column '{col}' not found in the DataFrame.")
            return
    # Convert 'Timestamp' column to datetime format
    cleaned_df['Timestamp'] = pd.to_datetime(cleaned_df['Timestamp'])
    # Set 'Timestamp' column as index
    cleaned_df.set_index('Timestamp', inplace=True)
    # Define colors
    colors = sns.color_palette("husl", len(columns_to_plot))
    # Plot time series
    fig, ax = plt.subplots(figsize=(12, 6))
    for i, col in enumerate(columns_to_plot):  # Specify columns to plot
        sns.lineplot(data=cleaned_df, x=cleaned_df.index, y=col, label=col, color=colors[i], linewidth=2, alpha=0.8, ax=ax)
    ax.set_xlabel('Time', fontsize=12)
    ax.set_ylabel('Value', fontsize=12)
    ax.set_title('Time Series Analysis for GHI, DNI, DHI', fontsize=16)
    ax.legend(fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.tick_params(axis='both', labelsize=10)
    plt.tight_layout()
    # Display the plot
    st.pyplot(fig)
# Function to plot time series for 'Tamb' column
def plot_time_series_tamb(cleaned_df):
    """Plot time series for 'Tamb' column."""
    # Check if 'Tamb' column is present in the DataFrame
    if 'Tamb' not in cleaned_df.columns:
        st.error("Error: 'Tamb' column not found in the DataFrame.")
        return
    if 'Timestamp' not in cleaned_df.columns:
        # If 'Timestamp' column is not present, use index as x-axis
        x_axis = cleaned_df.index
    else:
        # Convert 'Timestamp' column to datetime format
        cleaned_df['Timestamp'] = pd.to_datetime(cleaned_df['Timestamp'])
        x_axis = 'Timestamp'
    # Plot time series
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=cleaned_df, x=x_axis, y='Tamb', ax=ax)
    ax.set_xlabel('Time', fontsize=12)
    ax.set_ylabel('Tamb', fontsize=12)
    ax.set_title('Time Series Analysis for Tamb', fontsize=16)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.tick_params(axis='both', labelsize=10)
    plt.tight_layout()
    # Display the plot
    st.pyplot(fig)
# Function for correlation analysis
def correlation_analysis(data):
    # Select relevant columns for correlation analysis
    relevant_columns = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB']
    relevant_data = data[relevant_columns]
    # Calculate correlation matrix
    correlation_matrix = relevant_data.corr()
    # Plot heatmap
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, ax=ax)
    ax.set_title('Correlation Heatmap')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0)
    st.pyplot(fig)
# Function to plot boxplot with outliers for solar radiation and temperature data
def plot_boxplot_outliers(data):
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
    st.pyplot(fig)
# Function for scatter plots
def plot_scatter_plots(data):
    # Define pairs of variables for scatter plots
    variable_pairs = [('GHI', 'Tamb'), ('WS', 'WSgust')]
    module_pairs = [('TModA', 'Tamb'), ('TModB', 'Tamb')]
    # Plot scatter plots for GHI vs Tamb and WS vs WSgust
    fig, axes = plt.subplots(nrows=1, ncols=len(variable_pairs), figsize=(15, 5))
    for i, pair in enumerate(variable_pairs):
        sns.scatterplot(data=data, x=pair[0], y=pair[1], ax=axes[i])
        axes[i].set_title(f'{pair[0]} vs {pair[1]}')
        axes[i].set_xlabel(pair[0])
        axes[i].set_ylabel(pair[1])
    plt.tight_layout()
    st.pyplot(fig)
    # Plot scatter plot for (TModA, TModB) with ambient temperature (Tamb)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=data, x='TModA', y='TModB', hue='Tamb', palette='coolwarm', ax=ax)
    ax.set_title('(TModA, TModB) with Ambient Temperature (Tamb)')
    ax.set_xlabel('TModA')
    ax.set_ylabel('TModB')
    ax.legend(title='Tamb')
    st.pyplot(fig)
# Function to plot histograms
# Function to plot histograms
# Function to plot histograms
# Function to plot histograms
def plot_histograms(data):
    print("Plotting histograms...")
    # Select variables for histograms
    variables = ['GHI', 'DNI', 'DHI', 'WS', 'Tamb']
    
    num_variables = len(variables)
    num_rows = (num_variables - 1) // 3 + 1  # Calculate the number of rows needed
    
    # Create a figure
    fig, axes = plt.subplots(nrows=num_rows, ncols=3, figsize=(14, num_rows * 4))
    
    for i, var in enumerate(variables, 1):
        row = (i - 1) // 3
        col = (i - 1) % 3
        sns.histplot(data[var], kde=True, color='skyblue', bins=30, ax=axes[row, col])
        axes[row, col].set_title(f'{var} Histogram')
        axes[row, col].set_xlabel(var)
        axes[row, col].set_ylabel('Frequency')
    
    # Hide any unused subplots
    for j in range(num_variables, num_rows * 3):
        fig.delaxes(axes.flatten()[j])

    plt.tight_layout()
    
    # Display the plot
    st.pyplot(fig)


# Main function
def main():
    st.title("Solar panel Installation Analysis")
    with st.sidebar:
        upload_file = st.file_uploader("Choose a file", type=["csv", "xlsx",'pdf'])

        if upload_file is None:
            st.info("Upload a file through the sidebar", icon="ℹ️")
            st.stop()

    Weather_Data = load_data(upload_file)

    if Weather_Data is not None:
        # Remove Timestamp column from the list of columns
        columns_without_timestamp = [col for col in Weather_Data.columns if col != 'Timestamp']

        col1, col2, col3 = st.columns([1, 1, 1])
        with col1.expander("Weather Data"):
            st.write(Weather_Data)

        # Basic Information
        with col2.expander("Description"):
            st.write(Weather_Data.describe())

        # Summary Statistics
        with col3.expander("Summary Statistics"):
            selected_column = st.selectbox("Select a column for statistical analysis", columns_without_timestamp, index=0)
            calculate_summary_stats(Weather_Data, selected_column)

        # Display the count of negative values
        with col1.expander("Negative Value Counts:"):
            st.write(count_negative_values(Weather_Data))
        with col2.expander("Missing Values count"):
            st.write(missing_values(Weather_Data))
            
        st.write("---")
        st.subheader("Time Series Plot")
        plot_time_series(Weather_Data)
        st.subheader("Time Series Plot for Tamb")
        plot_time_series_tamb(Weather_Data)
    col6,col7 = st.columns(2)
    with col6:
        st.subheader("Correlation:")
        correlation_analysis(Weather_Data)
    with col7:
        st.subheader("outlier")
        plot_boxplot_outliers(Weather_Data)
    st.subheader("Scatter")
    plot_scatter_plots(Weather_Data)
    st.subheader("Histograms")
    plot_histograms(Weather_Data)
if __name__ == "__main__":
    main()
