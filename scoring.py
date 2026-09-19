from flask import Flask, session, jsonify, request
import pandas as pd
import numpy as np
import pickle
import os
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import json



################# Load config.json and get path variables
with open('config.json','r') as f:
    config = json.load(f) 

dataset_csv_path = os.path.join(config['output_folder_path']) 
test_data_path = os.path.join(config['test_data_path']) 


################# Function for model scoring
def score_model(model, dataframe, score_path=None):
    # Calculate and return the supplied model's F1 score on the supplied DataFrame.
    # Step 2: use the output_model_path model and test_data_path/testdata.csv.
    # API: use the deployed model and test_data_path/testdata.csv.
    # Drift check: use the same deployed model and newly ingested data.
    # Write latestscore.txt only when score_path is supplied; API and drift checks
    # must not overwrite the deployed baseline score.

