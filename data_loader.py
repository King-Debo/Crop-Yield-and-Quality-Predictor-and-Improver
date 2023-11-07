# Import the necessary libraries and modules
import pandas as pd # For reading and manipulating the data in tabular form
import geopandas as gpd # For reading and manipulating the data in spatial form
import numpy as np # For transforming the data into numpy arrays
import tkinter as tk # For creating the file dialog
import tkinter.filedialog as fd # For creating the file dialog

# Define the data loader function that preprocesses and transforms the data
def data_loader(data_type):
    # Create a file dialog to select the data file
    file_name = fd.askopenfilename(title=f"Select {data_type} Data File")

    # Check if the file name is valid
    if file_name:
        # Read the data file according to the data type
        if data_type == "Soil":
            # Read the soil data file as a geo data frame
            soil_data = gpd.read_file(file_name)

            # Inspect the soil data
            print(soil_data.head())
            print(soil_data.info())
            print(soil_data.describe())

            # Handle any missing, incomplete, or inaccurate data
            # For example, drop any rows or columns that have more than 50% missing values
            soil_data = soil_data.dropna(axis=0, thresh=0.5 * len(soil_data.columns))
            soil_data = soil_data.dropna(axis=1, thresh=0.5 * len(soil_data))

            # Merge the soil data with other data sources if needed
            # For example, merge the soil data with the weather data on the location column
            # soil_data = soil_data.merge(weather_data, on="location")

            # Transform the soil data into a suitable format for the predictive model
            # For example, transform the soil data into a numpy array of numerical values
            soil_data = soil_data.to_numpy()

            # Return the soil data
            return soil_data

        elif data_type == "Weather":
            # Read the weather data file as a data frame
            weather_data = pd.read_csv(file_name)

            # Inspect the weather data
            print(weather_data.head())
            print(weather_data.info())
            print(weather_data.describe())

            # Handle any missing, incomplete, or inaccurate data
            # For example, fill any missing values with the mean, median, or mode of the column
            weather_data = weather_data.fillna(weather_data.mean())

            # Merge the weather data with other data sources if needed
            # For example, merge the weather data with the satellite data on the date column
            # weather_data = weather_data.merge(satellite_data, on="date")

            # Transform the weather data into a suitable format for the predictive model
            # For example, transform the weather data into a numpy array of numerical values
            weather_data = weather_data.to_numpy()

            # Return the weather data
            return weather_data

        elif data_type == "Satellite":
            # Read the satellite data file as a geo data frame
            satellite_data = gpd.read_file(file_name)

            # Inspect the satellite data
            print(satellite_data.head())
            print(satellite_data.info())
            print(satellite_data.describe())

            # Handle any missing, incomplete, or inaccurate data
            # For example, replace any negative or zero values with a small positive value
            satellite_data = satellite_data.replace(0, 0.01)
            satellite_data = satellite_data.replace(-np.inf, 0.01)

            # Merge the satellite data with other data sources if needed
            # For example, merge the satellite data with the soil data on the geometry column
            # satellite_data = satellite_data.overlay(soil_data, how="intersection")

            # Transform the satellite data into a suitable format for the predictive model
            # For example, transform the satellite data into a numpy array of numerical values
            satellite_data = satellite_data.to_numpy()

            # Return the satellite data
            return satellite_data

        else:
            # Raise an exception if the data type is invalid
            raise ValueError(f"Invalid data type: {data_type}")
    else:
        # Raise an exception if the file name is invalid
        raise FileNotFoundError(f"No file selected")
