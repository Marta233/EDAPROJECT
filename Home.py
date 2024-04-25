import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
from src import eda_utils
st.set_page_config(page_title="Sales Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide"
                   )
st.title("Sales Dashboard")
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
            st.warning("PDF file format is not supported for direct loading.")
            return None
        else:
            st.error("Unsupported file format. Please upload a CSV, XLSX, or PDF file.")
            return None
    except Exception as e:
        st.error(f"An error occurred while loading the data: {str(e)}")
        return None

with st.sidebar:
    upload_file = st.file_uploader("Choose a file", type=["csv", "xlsx",'pdf'])

    if upload_file is None:
        st.info("upload file through config",icon="ℹ️")
        st.stop()

Weather_Data = load_data(upload_file) 

col1, col2, col3 = st.columns([1,1,1])
with col1.expander("Weather_Data"):
    st.write(Weather_Data)

