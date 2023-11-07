# Import the necessary libraries and modules
import tkinter as tk # For creating the user interface
import data_loader # For creating the data loader function
import predictive_model # For creating the predictive model function
import parameter_controller # For creating the parameter controller function
import evaluator # For creating the evaluator function
import saver # For creating the saver function
import loader # For creating the loader function

# Define the user interface function that creates and arranges the widgets on the window
def user_interface(window):
    # Create a frame for the data input widgets
    data_frame = tk.Frame(window)
    data_frame.pack(padx=10, pady=10)

    # Create a label for the data input widgets
    data_label = tk.Label(data_frame, text="Please input the data from various sources:")
    data_label.pack()

    # Create a button for the soil data input widget
    soil_button = tk.Button(data_frame, text="Soil Data", command=load_soil_data)
    soil_button.pack(side=tk.LEFT, padx=5, pady=5)

    # Create a button for the weather data input widget
    weather_button = tk.Button(data_frame, text="Weather Data", command=load_weather_data)
    weather_button.pack(side=tk.LEFT, padx=5, pady=5)

    # Create a button for the satellite data input widget
    satellite_button = tk.Button(data_frame, text="Satellite Data", command=load_satellite_data)
    satellite_button.pack(side=tk.LEFT, padx=5, pady=5)

    # Create a frame for the prediction and recommendation widgets
    pred_rec_frame = tk.Frame(window)
    pred_rec_frame.pack(padx=10, pady=10)

    # Create a label for the prediction and recommendation widgets
    pred_rec_label = tk.Label(pred_rec_frame, text="Please choose the type of prediction and recommendation:")
    pred_rec_label.pack()

    # Create a variable for the prediction and recommendation widgets
    pred_rec_var = tk.StringVar()
    pred_rec_var.set("Yield and Quality")

    # Create a radio button for the yield and quality prediction and recommendation widget
    yield_quality_radio = tk.Radiobutton(pred_rec_frame, text="Yield and Quality", variable=pred_rec_var, value="Yield and Quality", command=update_pred_rec)
    yield_quality_radio.pack(side=tk.LEFT, padx=5, pady=5)

    # Create a radio button for the yield prediction and recommendation widget
    yield_radio = tk.Radiobutton(pred_rec_frame, text="Yield", variable=pred_rec_var, value="Yield", command=update_pred_rec)
    yield_radio.pack(side=tk.LEFT, padx=5, pady=5)

    # Create a radio button for the quality prediction and recommendation widget
    quality_radio = tk.Radiobutton(pred_rec_frame, text="Quality", variable=pred_rec_var, value="Quality", command=update_pred_rec)
    quality_radio.pack(side=tk.LEFT, padx=5, pady=5)

    # Create a frame for the parameter controller widgets
    param_frame = tk.Frame(window)
    param_frame.pack(padx=10, pady=10)

    # Create a label for the parameter controller widgets
    param_label = tk.Label(param_frame, text="Please adjust the parameters of the predictive model:")
    param_label.pack()

    # Create a label and an entry for the crop type parameter controller widget
    crop_type_label = tk.Label(param_frame, text="Crop Type:")
    crop_type_label.grid(row=0, column=0, padx=5, pady=5)
    crop_type_var = tk.StringVar()
    crop_type_var.set("Wheat")
    crop_type_entry = tk.Entry(param_frame, textvariable=crop_type_var)
    crop_type_entry.grid(row=0, column=1, padx=5, pady=5)

    # Create a label and an entry for the location parameter controller widget
    location_label = tk.Label(param_frame, text="Location:")
    location_label.grid(row=1, column=0, padx=5, pady=5)
    location_var = tk.StringVar()
    location_var.set("India")
    location_entry = tk.Entry(param_frame, textvariable=location_var)
    location_entry.grid(row=1, column=1, padx=5, pady=5)

    # Create a label and a slider for the season parameter controller widget
    season_label = tk.Label(param_frame, text="Season:")
    season_label.grid(row=2, column=0, padx=5, pady=5)
    season_var = tk.IntVar()
    season_var.set(1)
    season_slider = tk.Scale(param_frame, from_=1, to=4, variable=season_var, orient=tk.HORIZONTAL)
    season_slider.grid(row=2, column=1, padx=5, pady=5)

    # Create a label and a checkbox for the irrigation parameter controller widget
    irrigation_label = tk.Label(param_frame, text="Irrigation:")
    irrigation_label.grid(row=3, column=0, padx=5, pady=5)
    irrigation_var = tk.BooleanVar()
    irrigation_var.set(True)
    irrigation_check = tk.Checkbutton(param_frame, variable=irrigation_var, onvalue=True, offvalue=False)
    irrigation_check.grid(row=3, column=1, padx=5, pady=5)

    # Create a button for the parameter controller widget
    param_button = tk.Button(param_frame, text="Update Prediction and Recommendation", command=update_pred_rec)
    param_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    # Create a frame for the result widgets
    result_frame = tk.Frame(window)
    result_frame.pack(padx=10, pady=10)

    # Create a label for the result widgets
    result_label = tk.Label(result_frame, text="The prediction and recommendation are:")
    result_label.pack()

    # Create a text widget for the prediction widget
    prediction_text = tk.Text(result_frame, width=40, height=10)
    prediction_text.pack(side=tk.LEFT, padx=5, pady=5)

    # Create a text widget for the recommendation widget
    recommendation_text = tk.Text(result_frame, width=40, height=10)
    recommendation_text.pack(side=tk.RIGHT, padx=5, pady=5)

    # Create a frame for the evaluator widgets
    evaluator_frame = tk.Frame(window)
    evaluator_frame.pack(padx=10, pady=10)

    # Create a label for the evaluator widgets
    evaluator_label = tk.Label(evaluator_frame, text="The accuracy and reliability of the prediction and recommendation are:")
    evaluator_label.pack()

    # Create a text widget for the evaluator widget
    evaluator_text = tk.Text(evaluator_frame, width=80, height=10)
    evaluator_text.pack(padx=5, pady=5)

    # Create a frame for the saver and loader widgets
    saver_loader_frame = tk.Frame(window)
    saver_loader_frame.pack(padx=10, pady=10)

    # Create a button for the saver widget
    saver_button = tk.Button(saver_loader_frame, text="Save Prediction and Recommendation", command=save_pred_rec)
    saver_button.pack(side=tk.LEFT, padx=5, pady=5)

    # Create a button for the loader widget
    loader_button = tk.Button(saver_loader_frame, text="Load Prediction and Recommendation", command=load_pred_rec)
    loader_button.pack(side=tk.RIGHT, padx=5, pady=5)
