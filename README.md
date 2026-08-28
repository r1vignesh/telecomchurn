# Telecom Customer Churn Prediction

A machine learning web app to predict customer churn for telecom companies.

## Live Demo
[Click here to view the app](https://telecomchurn-ptu5.onrender.com)

## Features
- Predict churn for individual customers
- View prediction history
- Explore the dataset
- Interactive dashboard with charts

## Tech Stack
- Python, Streamlit
- Scikit-learn, Imbalanced-learn
- Pandas, Plotly, Seaborn

## Models Used
- Logistic Regression
- Random Forest
- AdaBoost

## Run Locally
```bash
pip install -r requirements.txt
streamlit run Home.py
```

## Project Structure
telecomchurn/
├── Data/
│ ├── Dataset.csv
│ └── history.csv
├── models/
│ ├── adaboost.joblib
│ ├── encoder.joblib
│ ├── logisticregression.joblib
│ └── randomforest.joblib
├── pages/
│ ├── 01_Predict.py
│ ├── 02_History.py
│ ├── 03_Data.py
│ └── 04_Dashboard.py
├── Home.py
└── requirements.txt

## Author
Vignesh R — PG Project
