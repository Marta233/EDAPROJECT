import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
# Step 10: Visualization - Wind Analysis
def wind_analysis(data):
    """Explore wind speed and wind direction data."""
    print("Wind Analysis:")
    # Basic statistics
    print("\nBasic Statistics:")
    print(data[['WS', 'WSgust', 'WSstdev', 'WD', 'WDstdev']].describe())
    
    # Wind Speed Analysis
    print("\nWind Speed Analysis")
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=data, x='Timestamp', y='WS', label='Wind Speed (m/s)')
    sns.lineplot(data=data, x='Timestamp', y='WSgust', label='Wind Gust Speed (m/s)')
    sns.lineplot(data=data, x='Timestamp', y='WSstdev', label='Wind Speed Std Dev (m/s)')
    plt.xlabel('Timestamp')
    plt.ylabel('Wind Speed (m/s)')
    plt.title('Wind Speed Analysis')
    plt.legend()

    # Wind Direction Analysis
    print("\nWind Direction Analysis")
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=data, x='Timestamp', y='WD', label='Wind Direction (°)')
    sns.lineplot(data=data, x='Timestamp', y='WDstdev', label='Wind Direction Std Dev (°)')
    plt.xlabel('Timestamp')
    plt.ylabel('Wind Direction (°)')
    plt.title('Wind Direction Analysis')
    plt.legend()
def temperature_analysis(data):
    """Compare module temperatures (TModA, TModB) with ambient temperature (Tamb)."""
    print("Temperature Analysis:")
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=data, x='Timestamp', y='Tamb', label='Ambient Temperature (°C)')
    sns.lineplot(data=data, x='Timestamp', y='TModA', label='Module Temperature A (°C)')
    sns.lineplot(data=data, x='Timestamp', y='TModB', label='Module Temperature B (°C)')
    plt.xlabel('Timestamp')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Analysis')
    plt.legend()
def plot_histograms(data):
    print("Plotting histograms...")
    """Create histograms for specified variables."""
    # Select variables for histograms
    variables = ['GHI', 'DNI', 'DHI', 'WS', 'Tamb', 'TModA', 'TModB']
    
    # Plot histograms
    plt.figure(figsize=(14, 10))
    for i, var in enumerate(variables, 1):
        plt.subplot(3, 3, i)
        sns.histplot(data[var], kde=True, color='skyblue', bins=30)
        plt.title(f'{var} Histogram')
        plt.xlabel(var)
        plt.ylabel('Frequency')
    plt.tight_layout()
def plot_scatter_plots(data):
    print("Plotting scatter plots...")
    """Generate scatter plots to explore relationships between pairs of variables."""
    # Define pairs of variables for scatter plots
    variable_pairs = [('GHI', 'Tamb'), ('WS', 'WSgust'), ('TModA', 'TModB')]
    
    # Plot scatter plots
    plt.figure(figsize=(12, 8))
    for i, pair in enumerate(variable_pairs, 1):
        plt.subplot(2, 2, i)
        sns.scatterplot(data=data, x=pair[0], y=pair[1])
        plt.title(f'{pair[0]} vs {pair[1]}')
        plt.xlabel(pair[0])
        plt.ylabel(pair[1])
    plt.tight_layout()
    plt.show()