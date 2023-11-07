# Import the necessary libraries and modules
import numpy as np # For transforming the data into numpy arrays
import sklearn # For calculating and displaying the metrics
import tkinter as tk # For creating the user interface

# Define the evaluator function that measures the accuracy and reliability of the prediction and recommendation
def evaluator(data, prediction, recommendation, pred_rec_type, evaluator_text):
    # Check the type of prediction and recommendation
    if pred_rec_type == "Yield and Quality":
        # Calculate the mean absolute error and the coefficient of determination for the prediction
        mae = sklearn.metrics.mean_absolute_error(data, prediction)
        r2 = sklearn.metrics.r2_score(data, prediction)

        # Calculate the recommendation score for the recommendation
        rec_score = recommendation_score(data, recommendation)

        # Display the metrics on the user interface
        evaluator_text.delete(1.0, tk.END)
        evaluator_text.insert(1.0, f"Mean Absolute Error: {mae}\n")
        evaluator_text.insert(2.0, f"Coefficient of Determination: {r2}\n")
        evaluator_text.insert(3.0, f"Recommendation Score: {rec_score}\n")

    elif pred_rec_type == "Yield":
        # Calculate the mean absolute error and the coefficient of determination for the prediction
        mae = sklearn.metrics.mean_absolute_error(data, prediction)
        r2 = sklearn.metrics.r2_score(data, prediction)

        # Calculate the recommendation score for the recommendation
        rec_score = recommendation_score(data, recommendation)

        # Display the metrics on the user interface
        evaluator_text.delete(1.0, tk.END)
        evaluator_text.insert(1.0, f"Mean Absolute Error: {mae}\n")
        evaluator_text.insert(2.0, f"Coefficient of Determination: {r2}\n")
        evaluator_text.insert(3.0, f"Recommendation Score: {rec_score}\n")

    elif pred_rec_type == "Quality":
        # Calculate the confusion matrix for the prediction
        cm = sklearn.metrics.confusion_matrix(data, prediction)

        # Calculate the recommendation score for the recommendation
        rec_score = recommendation_score(data, recommendation)

        # Display the metrics on the user interface
        evaluator_text.delete(1.0, tk.END)
        evaluator_text.insert(1.0, f"Confusion Matrix: \n{cm}\n")
        evaluator_text.insert(2.0, f"Recommendation Score: {rec_score}\n")

    else:
        # Raise an exception if the type of prediction and recommendation is invalid
        raise ValueError(f"Invalid type of prediction and recommendation: {pred_rec_type}")
