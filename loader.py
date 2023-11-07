# Import the necessary libraries and modules
import pandas as pd # For loading the prediction and the recommendation from a tabular format
import geopandas as gpd # For loading the prediction and the recommendation from a spatial format
import sqlite3 # For loading the prediction and the recommendation from a relational database
import pymongo # For loading the prediction and the recommendation from a non-relational database
import tkinter as tk # For creating the file dialog
import tkinter.filedialog as fd # For creating the file dialog

# Define the loader function that loads the prediction and the recommendation
def loader(pred_rec_type):
    # Create a file dialog to select the file name and location
    file_name = fd.askopenfilename(title="Load Prediction and Recommendation")

    # Check if the file name is valid
    if file_name:
        # Load the prediction and the recommendation from a file according to the file extension
        if file_name.endswith(".csv"):
            # Load the prediction and the recommendation from a csv file
            # Read the csv file as a data frame
            pred_rec_df = pd.read_csv(file_name)
            # Split the data frame into prediction and recommendation data frames
            prediction_df = pred_rec_df[["Yield", "Quality"]]
            recommendation_df = pred_rec_df[["Action", "Intervention"]]
            # Convert the prediction and recommendation data frames into numpy arrays
            prediction = prediction_df.to_numpy()
            recommendation = recommendation_df.to_numpy()

        elif file_name.endswith(".json"):
            # Load the prediction and the recommendation from a json file
            # Read the json file as a data frame
            pred_rec_df = pd.read_json(file_name, orient="records")
            # Split the data frame into prediction and recommendation data frames
            prediction_df = pred_rec_df[["Yield", "Quality"]]
            recommendation_df = pred_rec_df[["Action", "Intervention"]]
            # Convert the prediction and recommendation data frames into numpy arrays
            prediction = prediction_df.to_numpy()
            recommendation = recommendation_df.to_numpy()

        elif file_name.endswith(".xlsx"):
            # Load the prediction and the recommendation from an excel file
            # Read the excel file as a data frame
            pred_rec_df = pd.read_excel(file_name)
            # Split the data frame into prediction and recommendation data frames
            prediction_df = pred_rec_df[["Yield", "Quality"]]
            recommendation_df = pred_rec_df[["Action", "Intervention"]]
            # Convert the prediction and recommendation data frames into numpy arrays
            prediction = prediction_df.to_numpy()
            recommendation = recommendation_df.to_numpy()

        elif file_name.endswith(".shp"):
            # Load the prediction and the recommendation from a shapefile
            # Read the shapefile as a geo data frame
            pred_rec_gdf = gpd.read_file(file_name)
            # Split the geo data frame into prediction and recommendation geo data frames
            prediction_gdf = pred_rec_gdf[["Yield", "Quality", "geometry"]]
            recommendation_gdf = pred_rec_gdf[["Action", "Intervention", "geometry"]]
            # Convert the prediction and recommendation geo data frames into numpy arrays
            prediction = prediction_gdf.to_numpy()
            recommendation = recommendation_gdf.to_numpy()

        else:
            # Raise an exception if the file extension is invalid
            raise ValueError(f"Invalid file extension: {file_name}")

        # Load the prediction and the recommendation from a database according to the user's choice
        # Ask the user if they want to load the prediction and the recommendation from a database
        db_choice = tk.messagebox.askyesno(title="Load Prediction and Recommendation from Database", message="Do you want to load the prediction and recommendation from a database?")

        # Check if the user's choice is yes
        if db_choice:
            # Ask the user to choose the type of database
            db_type = tk.simpledialog.askstring(title="Choose Database Type", prompt="Please choose the type of database: sqlite or mongodb")

            # Check the type of database
            if db_type == "sqlite":
                # Load the prediction and the recommendation from a sqlite database
                # Create a connection to the sqlite database
                conn = sqlite3.connect("pred_rec.db")
                # Create a cursor object
                cur = conn.cursor()
                # Select the prediction and the recommendation from the table
                cur.execute("""SELECT yield, quality, action, intervention FROM pred_rec""")
                # Fetch the prediction and the recommendation as a list of tuples
                pred_rec_list = cur.fetchall()
                # Convert the prediction and the recommendation list into numpy arrays
                prediction = np.array([row[:2] for row in pred_rec_list])
                recommendation = np.array([row[2:] for row in pred_rec_list])
                # Close the connection to the database
                conn.close()

            elif db_type == "mongodb":
                # Load the prediction and the recommendation from a mongodb database
                # Create a connection to the mongodb database
                client = pymongo.MongoClient("mongodb://localhost:27017/")
                # Access the database for the prediction and the recommendation
                db = client["pred_rec"]
                # Access the collection for the prediction and the recommendation
                col = db["pred_rec"]
                # Select the prediction and the recommendation from the collection
                pred_rec_list = col.find()
                # Convert the prediction and the recommendation list into numpy arrays
                prediction = np.array([[doc["yield"], doc["quality"]] for doc in pred_rec_list])
                recommendation = np.array([[doc["action"], doc["intervention"]] for doc in pred_rec_list])
                # Close the connection to the database
                client.close()

            else:
                # Raise an exception if the type of database is invalid
                raise ValueError(f"Invalid type of database: {db_type}")

        # Return the prediction and the recommendation
        return prediction, recommendation
    else:
        # Raise an exception if the file name is invalid
        raise FileNotFoundError(f"No file selected")
