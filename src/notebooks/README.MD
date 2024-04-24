# Solar Energy Data Analysis

## Overview

This project aims to analyze solar energy data collected from various weather stations to understand solar radiation patterns, temperature variations, wind characteristics, and their correlations. The analysis provides insights into solar energy potential, weather conditions, and their impact on energy generation.

## Data

The dataset used in this project contains the following columns:

- **Timestamp**: Date and time of the data recording.
- **GHI (Global Horizontal Irradiance)**: Total solar radiation received on a horizontal surface.
- **DNI (Direct Normal Irradiance)**: Solar radiation received in a plane perpendicular to the sun's rays.
- **DHI (Diffuse Horizontal Irradiance)**: Solar radiation received from the sky (excluding direct sunlight).
- **Tamb (Ambient Temperature)**: Temperature of the air surrounding the solar panels.
- **TModA (Module Temperature A)**: Temperature of solar module A.
- **TModB (Module Temperature B)**: Temperature of solar module B.
- **WS (Wind Speed)**: Speed of the wind.
- **WSgust (Wind Gust Speed)**: Maximum wind speed recorded during the time interval.
- **WSstdev (Wind Speed Standard Deviation)**: Standard deviation of wind speed.
- **WD (Wind Direction)**: Direction from which the wind is blowing.
- **WDstdev (Wind Direction Standard Deviation)**: Standard deviation of wind direction.

## Analysis

The analysis includes the following steps:

1. **Basic Information**: Display basic information about the dataset, such as the number of entries and column data types.
2. **Descriptive Statistics**: Calculate summary statistics for numeric columns to understand the distribution of data.

3. **Missing Values**: Identify missing values in the dataset and handle them appropriately.

4. **Negative Values**: Identify and handle negative values, if any, in the dataset.

5. **Time Series Analysis**: Plot time series data for solar radiation, temperature, and wind variables to observe trends over time.

6. **Correlation Analysis**: Examine correlations between solar radiation, temperature, and wind variables to understand their relationships.

7. **Outlier Detection**: Identify outliers in the data using box plots and histograms.

8. **Histograms**: Visualize the frequency distribution of various variables using histograms.

9. **Scatter Plots**: Explore relationships between pairs of variables using scatter plots.

## Usage

To run the analysis, follow these steps:

1. Install the required dependencies:

   ```bash
   pip install pandas matplotlib seaborn
   ```

2. Clone the repository:

   ```bash
   git clone https://github.com/Marta233/EDAPROJECT.git
   ```

3. Navigate to the project directory:

   ```bash
   cd EDAPROJECT
   ```

4. Run the main script:

   ```bash
   python run_eda_for_benin.py
   python run_eda_for_sieeraleoone.py
   python run_eda_for_togo.py
   ```

5. View the generated plots and analysis results.

## Contributing

Contributions to this project are welcome! If you have suggestions, feature requests, or find any issues, feel free to open an issue or create a pull request.

## License

Marta A.
