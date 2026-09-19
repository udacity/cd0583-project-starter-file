from flask import Flask, session, jsonify, request
import pandas as pd
import numpy as np
import pickle
import json
import os



###################### Set up variables for use in our script
app = Flask(__name__)
app.secret_key = '1652d576-484a-49fd-913a-6879acfa6ba4'

with open('config.json','r') as f:
    config = json.load(f) 

dataset_csv_path = os.path.join(config['output_folder_path']) 

prediction_model = None


####################### Prediction Endpoint
@app.route("/prediction", methods=['POST','OPTIONS'])
def predict():        
    # Load the dataset at the location supplied in the request into a DataFrame,
    # then pass it to the Step 3 model_predictions function (deployed model).
    return # Add return value for prediction outputs

####################### Scoring Endpoint
@app.route("/scoring", methods=['GET','OPTIONS'])
def scoring_endpoint():
    # Score the deployed model on test_data_path/testdata.csv using score_model.
    # Do not overwrite the deployed baseline score.
    return # Add return value (a single F1 score number)

####################### Summary Statistics Endpoint
@app.route("/summarystats", methods=['GET','OPTIONS'])
def summarystats_endpoint():
    # Return means, medians, and standard deviations for numeric columns.
    return # Return a list of all calculated summary statistics

####################### Diagnostics Endpoint
@app.route("/diagnostics", methods=['GET','OPTIONS'])
def diagnostics_endpoint():
    # Return ingestion/training timings, missing-value percentages for all columns,
    # and the dependency version table. Do not replace the deployed model.
    return # Add return value for all diagnostics

if __name__ == "__main__":    
    app.run(host='0.0.0.0', port=8000, debug=True, threaded=True)
