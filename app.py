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
    # Call the prediction function you created in Step 3
    return # Add return value for prediction outputs

####################### Scoring Endpoint
@app.route("/scoring", methods=['GET','OPTIONS'])
def scoring_endpoint():
    # Check the score of the deployed model
    return # Add return value (a single F1 score number)

####################### Summary Statistics Endpoint
@app.route("/summarystats", methods=['GET','OPTIONS'])
def summarystats_endpoint():
    # Check means, medians, and modes for each column
    return # Return a list of all calculated summary statistics

####################### Diagnostics Endpoint
@app.route("/diagnostics", methods=['GET','OPTIONS'])
def diagnostics_endpoint():
    # Check timing and percent NA values
    return # Add return value for all diagnostics

if __name__ == "__main__":    
    app.run(host='0.0.0.0', port=8000, debug=True, threaded=True)
