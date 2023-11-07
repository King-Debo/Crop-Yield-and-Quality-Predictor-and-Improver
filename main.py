# Import the necessary libraries and modules
import tkinter as tk # For creating the user interface
import ui # For creating the user interface function
import data_loader # For creating the data loader function
import predictive_model # For creating the predictive model function
import parameter_controller # For creating the parameter controller function
import evaluator # For creating the evaluator function
import saver # For creating the saver function
import loader # For creating the loader function

# Define the main function that runs the program
def main():
    # Create a main window for the user interface
    window = tk.Tk()
    window.title("Crop Yield and Quality Predictor and Improver")
    window.geometry("800x600")

    # Call the user interface function from the ui module
    ui.user_interface(window)

    # Start the main loop of the window
    window.mainloop()

# Call the main function
if __name__ == "__main__":
    main()
