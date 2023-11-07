# Import the necessary libraries and modules
import tkinter as tk # For creating the user interface
import predictive_model # For creating the predictive model function

# Define the parameter controller function that updates the prediction and recommendation based on the new values of the parameters
def parameter_controller(window, data, pred_rec_type, crop_type_var, location_var, season_var, irrigation_var, prediction_text, recommendation_text):
    # Get the new values of the parameters from the user interface
    crop_type = crop_type_var.get()
    location = location_var.get()
    season = season_var.get()
    irrigation = irrigation_var.get()

    # Call the predictive model function from the predictive_model module with the new values of the parameters
    prediction, recommendation = predictive_model.predictive_model(data, pred_rec_type, crop_type, location, season, irrigation)

    # Display the updated prediction and recommendation on the user interface
    prediction_text.delete(1.0, tk.END)
    prediction_text.insert(1.0, prediction)
    recommendation_text.delete(1.0, tk.END)
    recommendation_text.insert(1.0, recommendation)
