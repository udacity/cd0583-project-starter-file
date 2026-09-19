
import pandas as pd
import numpy as np
import timeit
import os
import json

################## Load config.json and get environment variables
with open('config.json','r') as f:
    config = json.load(f) 

dataset_csv_path = os.path.join(config['output_folder_path']) 
test_data_path = os.path.join(config['test_data_path']) 

################## Function to get model predictions
def model_predictions(dataframe):
    # Read the model from prod_deployment_path and predict for the supplied DataFrame.
    # Select the same predictor columns used for training; do not include the target.
    return # Return value should be a list containing all predictions

################## Function to get summary statistics
def dataframe_summary():
    # Read the ingested dataset from output_folder_path. For each numeric column,
    # calculate mean, median, and standard deviation.
    return # Return value should be a list containing all summary statistics

################## Function to check missing data
def missing_data():
    # Calculate missing-value percentages for every ingested dataset column,
    # including nonnumeric columns, and return a list in column order.
    return

##################Function to get timings
def execution_time():
    # Time ingestion.py and training.py, in that order, as required by Step 3
    # and the rubric. Isolate timing outputs; do not replace the deployed model.
    return # Return a list of 2 timing values in seconds

################## Function to check dependencies
def outdated_packages_list():
    # Report every dependency used by the project in a three-column table:
    # package name, installed version, and latest available version. Do not upgrade.


if __name__ == '__main__':
    # Load test_data_path/testdata.csv into a DataFrame and pass it to model_predictions.
    dataframe_summary()
    missing_data()
    execution_time()
    outdated_packages_list()





    
