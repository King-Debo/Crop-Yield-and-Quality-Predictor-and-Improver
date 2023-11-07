# Import the necessary libraries and modules
import pandas as pd # For saving the prediction and the recommendation in a tabular format
import geopandas as gpd # For saving the prediction and the recommendation in a spatial format
import sqlite3 # For saving the prediction and the recommendation in a relational database
import pymongo # For saving the prediction and the recommendation in a non-relational database
import tkinter as tk # For creating the file dialog
import tkinter.filedialog as fd # For creating the file dialog

# Define the saver function that saves the prediction and the recommendation
def saver(prediction, recommendation, pred_rec_type):
    # Create a file dialog to select the file name and location
    file_name = fd.asksaveasfilename(title="Save Prediction and Recommendation")

    # Check if the file name is valid
    if file_name:
        # Save the prediction and the recommendation in a file according to the file extension
        if file_name.endswith(".csv"):
            # Save the prediction and the recommendation in a csv file
            # Convert the prediction and the recommendation into data frames
            prediction_df = pd.DataFrame(prediction, columns=["Yield", "Quality"])
            recommendation_df = pd.DataFrame(recommendation, columns=["Action", "Intervention"])
            # Concatenate the prediction and the recommendation data frames
            pred_rec_df = pd.concat([prediction_df, recommendation_df], axis=1)
            # Write the prediction and the recommendation data frame to a csv file
            pred_rec_df.to_csv(file_name, index=False)

        elif file_name.endswith(".json"):
            # Save the prediction and the recommendation in a json file
            # Convert the prediction and the recommendation into data frames
            prediction_df = pd.DataFrame(prediction, columns=["Yield", "Quality"])
            recommendation_df = pd.DataFrame(recommendation, columns=["Action", "Intervention"])
            # Concatenate the prediction and the recommendation data frames
            pred_rec_df = pd.concat([prediction_df, recommendation_df], axis=1)
            # Write the prediction and the recommendation data frame to a json file
            pred_rec_df.to_json(file_name, orient="records")

        elif file_name.endswith(".xlsx"):
            # Save the prediction and the recommendation in an excel file
            # Convert the prediction and the recommendation into data frames
            prediction_df = pd.DataFrame(prediction, columns=["Yield", "Quality"])
            recommendation_df = pd.DataFrame(recommendation, columns=["Action", "Intervention"])
            # Create a writer object for the excel file
            writer = pd.ExcelWriter(file_name, engine="xlsxwriter")
            # Write the prediction and the recommendation data frames to separate sheets in the excel file
            prediction_df.to_excel(writer, sheet_name="Prediction", index=False)
            recommendation_df.to_excel(writer, sheet_name="Recommendation", index=False)
            # Save the excel file
            writer.save()

        elif file_name.endswith(".shp"):
            # Save the prediction and the recommendation in a shapefile
            # Convert the prediction and the recommendation into geo data frames
            prediction_gdf = gpd.GeoDataFrame(prediction, columns=["Yield", "Quality", "geometry"])
            recommendation_gdf = gpd.GeoDataFrame(recommendation, columns=["Action", "Intervention", "geometry"])
            # Overlay the prediction and the recommendation geo data frames
            pred_rec_gdf = gpd.overlay(prediction_gdf, recommendation_gdf, how="intersection")
            # Write the prediction and the recommendation geo data frame to a shapefile
            pred_rec_gdf.to_file(file_name)

        else:
            # Raise an exception if the file extension is invalid
            raise ValueError(f"Invalid file extension: {file_name}")

        # Save the prediction and the recommendation in a database according to the user's choice
        # Ask the user if they want to save the prediction and the recommendation in a database
        db_choice = tk.messagebox.askyesno(title="Save Prediction and Recommendation in Database", message="Do you want to save the prediction and recommendation in a database?")

        # Check if the user's choice is yes
        if db_choice:
            # Ask the user to choose the type of database
            db_type = tk.simpledialog.askstring(title="Choose Database Type", prompt="Please choose the type of database: sqlite or mongodb")

            # Check the type of database
            if db_type == "sqlite":
                # Save the prediction and the recommendation in a sqlite database
                # Create a connection to the sqlite database
                conn = sqlite3.connect("pred_rec.db")
                # Create a cursor object
                cur = conn.cursor()
                # Create a table for the prediction and the recommendation
                cur.execute("""CREATE TABLE IF NOT EXISTS pred_rec (
                    id INTEGER PRIMARY KEY,
                    yield REAL,
                    quality INTEGER,
                    action TEXT,
                    intervention TEXT
                )""")
                # Insert the prediction and the recommendation into the table
                for i in range(len(prediction)):
                    cur.execute("""INSERT INTO pred_rec (yield, quality, action, intervention) VALUES (?, ?, ?, ?)""",
                        (prediction[i][0], prediction[i][1], recommendation[i][0], recommendation[i][1]))
                # Save the changes to the database
                conn.commit()
                # Close the connection to the database
                conn.close()

            elif db_type == "mongodb":
                # Save the prediction and the recommendation in a mongodb database
                # Create a connection to the mongodb database
                client = pymongo.MongoClient("mongodb://localhost:27017/")
                # Create a database for the prediction and the recommendation
                db = client["pred_rec"]
                # Create a collection for the prediction and the recommendation
                col = db["pred_rec"]
                # Insert the prediction and the recommendation into the collection
                for i in range(len(prediction)):
                    col.insert_one({
                        "yield": prediction[i][0],
                        "quality": prediction[i][1],
                        "action": recommendation[i][0],
                        "intervention": recommendation[i][1]
                    })
                # Close the connection to the database
                client.close()

            else:
                # Raise an exception if the type of database is invalid
                raise ValueError(f"Invalid type of database: {db_type}")
    else:
        # Raise an exception if the file name is invalid
        raise FileNotFoundError(f"No file selected")
