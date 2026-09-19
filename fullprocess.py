import training
import scoring
import deployment
import diagnostics
import reporting

################## Check and read new data
# Read ingestedfiles.txt from prod_deployment_path.

# Compare the input_folder_path files with that deployed ingestion record.
# For this stage, use sourcedata as input_folder_path and models as output_model_path.



################## Deciding whether to proceed, part 1
# If no new files are found, stop without training or deploying.
# Otherwise, run ingestion to update the dataset and local ingestedfiles.txt.


################## Checking for model drift
# Read the baseline latestscore.txt and model from prod_deployment_path.
# Score that SAME deployed model on the newly ingested data, before any training.
# Pass the model and data explicitly to score_model; preserve the deployed baseline.


################## Deciding whether to proceed, part 2
# Proceed only if the new F1 score is LOWER than the deployed baseline score.
# If it is equal or higher, stop without training or deploying.



################## Re-deployment
# Train a replacement model on the newly ingested data only after detecting drift.
# Score the replacement on test_data_path/testdata.csv, saving latestscore.txt
# under output_model_path. Deploy the replacement model, its new score, and the
# updated ingestedfiles.txt together by running deployment.py.

################## Diagnostics and reporting
# Run reporting.py for the newly deployed model and save confusionmatrix2.png.
# With the API running, run apicalls.py to make real HTTP requests to all four
# endpoints and save their combined responses as apireturns2.txt.







