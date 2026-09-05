# Visit with Us — Wellness Tourism MLOps

## Structure

visit-with-us-mlops/
├── data/tourism.csv
├── artifacts/train.csv
├── artifacts/test.csv
├── artifacts/experiment.json
├── artifacts/metrics.json
├── models/wellness_tourism_model.joblib
├── scripts/validate_data.py
├── app/app.py
├── app/requirements.txt
├── .github/workflows/pipeline.yml
└── assignment.ipynb

## Local deployment
pip install -r app/requirements.txt
streamlit run app/app.py

## CI/CD
GitHub Actions validates the dataset, creates train/test artifacts, tunes and evaluates the Random Forest, saves the best model, and commits updated model artifacts to main on direct pushes.
