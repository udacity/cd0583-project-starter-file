# A Dynamic Risk Assessment System

Starter files for the **A Dynamic Risk Assessment System** project in Udacity's **ML Model Scoring and Monitoring** course (`cd0583`). Build a workflow that trains, deploys, evaluates, and monitors a model for corporate-client attrition risk.

This repository contains **unfinished templates**, not a completed solution. Several files intentionally contain blank assignments or incomplete function bodies and will raise syntax errors until you implement them. Installing dependencies alone does not make the pipeline runnable.

Follow the [project classroom](https://learn.udacity.com/cd0583?version=1.2&lessonKey=f247329b-1a30-4dd7-807f-ef12cd975ae3&conceptKey=d7b9b451-4ee0-4b5d-bd99-64f5a67c44fd) and its rubric for the full requirements and submission instructions. Classroom access requires enrollment.

## Set up your environment

Clone the repository and work from its root directory; the templates load `config.json` and data using relative paths.

```bash
git clone https://github.com/udacity/cd0583-project-starter-file.git
cd cd0583-project-starter-file
```

### Development container

The repository includes a Python 3.14 development-container configuration. With Docker and the VS Code Dev Containers extension available, open the repository and select **Dev Containers: Reopen in Container**. In the container terminal, install the dependencies:

```bash
python -m pip install -r requirements.txt
python -m pip check
```

The container configuration does not install dependencies automatically.

### Local Python environment

The dependency set has been checked with Python 3.14.3 on Linux ARM64. Other platforms have not been runtime-verified for this starter.

On macOS or Linux, create and activate a virtual environment:

```bash
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip check
```

**Windows checkout note:** the repository currently contains macOS metadata files named `Icon` followed by a carriage return. Native Windows checkout can fail on these paths; see [issue #8](https://github.com/udacity/cd0583-project-starter-file/issues/8). A Linux filesystem inside WSL or a Linux-based workspace avoids Windows filename restrictions.

## Repository layout

| File or directory | Purpose |
| --- | --- |
| `ingestion.py` | Implement data ingestion and ingestion records. |
| `training.py` | Implement model training and model persistence. |
| `scoring.py` | Implement model scoring. |
| `deployment.py` | Implement deployment of the model and associated records. |
| `diagnostics.py` | Implement predictions, dataset statistics, missing-data checks, timing, and dependency diagnostics. |
| `reporting.py` | Implement model-performance reports. |
| `app.py` | Implement the Flask API endpoints. |
| `apicalls.py` | Implement API calls and save their combined responses. |
| `fullprocess.py` | Implement the new-data and model-drift automation workflow. |
| `wsgi.py` | Expose the Flask application to a WSGI server. |
| `config.json` | Configure input, output, test-data, and deployment paths. |
| `requirements.txt` | Pin the project's Python dependencies. |
| `practicedata/` | Supplied practice inputs: `dataset1.csv` and `dataset2.csv`. |
| `sourcedata/` | Supplied source inputs: `dataset3.csv` and `dataset4.csv`. |
| `testdata/` | Supplied evaluation input: `testdata.csv`. |
| `ingesteddata/` | Destination for your ingestion outputs. |
| `practicemodels/` | Destination for your practice models and reports. |
| `models/` | Destination for your later-stage models and reports. |
| `production_deployment/` | Destination for your deployed model and associated records. |

The five supplied CSV files contain fabricated corporate data. The four output directories initially contain only `.gitkeep` files; these preserve the directory structure and are not input data.

## Configuration

The starter begins with practice paths:

| Setting | Initial value |
| --- | --- |
| `input_folder_path` | `practicedata` |
| `output_folder_path` | `ingesteddata` |
| `test_data_path` | `testdata` |
| `output_model_path` | `practicemodels` |
| `prod_deployment_path` | `production_deployment` |

For the process-automation stage, follow the classroom instructions to switch `input_folder_path` to `sourcedata` and `output_model_path` to `models`. Keep the directory structure consistent when using a local environment or the Udacity Workspace.

## Complete the project

1. **Data ingestion:** combine the input CSV data and record which files were ingested.
2. **Training, scoring, and deployment:** train and evaluate a model, then deploy it with its score and ingestion records.
3. **Diagnostics:** implement prediction, data-quality, timing, and dependency checks.
4. **Reporting and API:** generate a confusion-matrix report, implement the endpoints below, and save their combined responses.
5. **Process automation:** check for new data, evaluate the deployed model on newly ingested data, and retrain and redeploy only when model drift requires it. Configure the required cron job according to the classroom instructions.

These are implementation tasks, not features already provided by the templates. Generated models, scores, reports, API responses, and a completed cron job are intentionally absent from the starter.

### API development

After implementing the required functions and creating the necessary data and model artifacts, start the development API from the repository root:

```bash
python app.py
```

The template uses port **8000**. In a second terminal using the same Python environment, run your completed `apicalls.py` against `http://127.0.0.1:8000`.

| Method | Endpoint | Intended response |
| --- | --- | --- |
| POST | `/prediction` | Predictions for the supplied dataset location. |
| GET | `/scoring` | The deployed model's score. |
| GET | `/summarystats` | Dataset summary statistics. |
| GET | `/diagnostics` | Timing, missing-data, and dependency diagnostics. |

The initial endpoint bodies do not return usable responses. Keep the model and data used by each endpoint consistent with the classroom requirements. The included Flask debug server is for development.

## Submission

Use the classroom rubric as the final checklist. Submit the required scripts and generated outputs in a ZIP, including the reports and cron-job record required by the project. The starter repository itself is not a completed submission.

## License

See [LICENSE](LICENSE) for the repository's license terms.
