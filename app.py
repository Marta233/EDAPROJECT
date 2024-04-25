import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from src import eda_utils
import Streamlit as st

# Set page title
st.title('Solar Energy Dashboard')
# Load data
@st.cache
def load_data(file_path):
    """Load data from a CSV file."""
    return pd.read_csv(file_path)

# Sidebar for file upload and customization
st.sidebar.title('Data Selection and Customization')

# File upload
# file = st.sidebar.file_uploader("Upload CSV", type=['csv'])
with st.sidebar:
    upload_file = st.file_uploader("Choose a file", type=["csv", "xlsx",'pdf'])

# Check if a file is uploaded
if file is not None:
    # Load data
    data = load_data(file)
    
    # Display basic information
    st.write('## Basic Information')
    eda_utils.basic_info(data)
    
    # Display basic description
    st.write('## Basic Description')
    eda_utils.basic_desc(data)
    
    # Display summary statistics
    st.write('## Summary Statistics')
    summary_stats_list = eda_utils.calculate_summary_stats(data)
    st.write(pd.DataFrame(summary_stats_list, columns=['Statistic', 'Description', 'Value']))
    
    # Display missing values
    st.write('## Missing Values')
    eda_utils.missing_values(data)
    
    # Display count of negative values
    st.write('## Count of Negative Values')
    eda_utils.count_negative_values(data)
    
    # Remove negative rows
    cleaned_data = eda_utils.remove_negative_rows(data, ['GHI', 'DNI', 'DHI'])
    
    # Display plot time series
    st.write('## Plot Time Series')
    eda_utils.plot_time_series(cleaned_data)
    st.pyplot()
    
    # Display correlation analysis
    st.write('## Correlation Analysis')
    eda_utils.correlation_analysis(cleaned_data)
    st.pyplot()
    
    # Display boxplot with outliers
    st.write('## Boxplot with Outliers')
    eda_utils.plot_boxplot_outliers(cleaned_data)
    st.pyplot()
