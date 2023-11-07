# Crop Yield and Quality Predictor and Improver

This project aims to create a program that can predict and improve the crop yield and quality based on various data sources, such as soil, weather, and satellite data. The program also allows the user to adjust the parameters of the predictive model, such as crop type, location, season, or irrigation, and provides recommendations on how to optimize the crop production.

## Files

The files needed for coding the project are:

- main.py: This file contains the main function that runs the program and calls the other functions from the other files.
- ui.py: This file contains the user interface function that allows the user to input the data from various sources, choose the type of prediction and recommendation, and set any other parameters or constraints.
- data_loader.py: This file contains the data loader function that preprocesses and transforms the data into a suitable format for the predictive model.
- predictive_model.py: This file contains the predictive model function that uses neural networks, random forests, or support vector machines to predict and improve the crop yield and quality based on the data.
- parameter_controller.py: This file contains the parameter controller function that allows the user to adjust the parameters of the predictive model such as crop type, location, season, or irrigation.
- evaluator.py: This file contains the evaluator function that measures the accuracy and reliability of the prediction and the recommendation using appropriate metrics such as mean absolute error, coefficient of determination, confusion matrix, etc.
- saver.py: This file contains the saver function that saves the prediction and the recommendation in a file or a database.
- loader.py: This file contains the loader function that loads the prediction and the recommendation from a file or a database.

## Libraries and Modules

The libraries and modules needed for coding the project are:

- tkinter: For creating the user interface
- pandas: For reading and manipulating the data in tabular form
- geopandas: For reading and manipulating the data in spatial form
- numpy: For transforming the data into numpy arrays
- sklearn: For creating and training the predictive model
- keras: For creating and training the neural network model
- tensorflow: For creating and training the neural network model
- sqlite3: For saving and loading the prediction and the recommendation in a relational database
- pymongo: For saving and loading the prediction and the recommendation in a non-relational database

## How to Run

To run the program, follow these steps:

1. Install the required libraries and modules using the command `pip install -r requirements.txt`
2. Run the main.py file using the command `python main.py`
3. Follow the instructions on the user interface to input the data, choose the type of prediction and recommendation, and set the parameters of the predictive model
4. View the prediction and the recommendation on the user interface, and evaluate their accuracy and reliability using the metrics
5. Save or load the prediction and the recommendation in a file or a database using the buttons on the user interface
