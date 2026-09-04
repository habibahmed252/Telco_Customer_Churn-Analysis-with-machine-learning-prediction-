# Telco_Customer_Churn-Analysis-with-machine-learning-prediction-
An end-to-end Customer Churn Analysis & Prediction project that combines Data Analysis, Power BI, Machine Learning, and Streamlit to understand customer behavior and predict potential churn.

🎯 Project Objective

The main goal of this project is to analyze customer data, identify the key factors associated with churn, build an accurate Machine Learning model to predict whether a customer is likely to churn, and deploy the model through an interactive Streamlit application.

🔄 Project Workflow

Data Cleaning → EDA → Power BI Dashboard → Data Preprocessing → Machine Learning → Model Evaluation → Streamlit Deployment

1. 🧹 Data Cleaning
Checked missing values and data types.
Handled missing values in TotalCharges.
Verified duplicate records and customer IDs.
Prepared the dataset for analysis and modeling.
Created meaningful customer tenure segments.
2. 📈 Exploratory Data Analysis

Performed EDA to understand customer behavior and discover patterns related to churn.

The analysis focused on:

Customer demographics
Tenure and contract type
Internet and subscribed services
Payment methods
Monthly and total charges
Churn distribution
Customer segments and churn patterns
3. 📊 Power BI Dashboard

Created an interactive Power BI dashboard to visualize important business insights.

The dashboard includes:

Overview
Customer Analysis
Services Analysis
Churn Risk Analysis
Payment Methods Analysis

Interactive slicers and visualizations allow users to explore churn patterns across different customer segments and services.

4. 🤖 Machine Learning Model

A Machine Learning classification model was developed to predict customer churn.

The ML workflow includes:

Feature selection
Categorical encoding
Numerical feature processing
Train/Test Split
Model training
Model evaluation
Churn prediction

The target variable is:

Churn → Yes / No

5. 🚀 Streamlit Deployment

The trained Machine Learning model was integrated into an interactive Streamlit web application.

Users can enter customer information and receive:

Churn prediction
Prediction probability
An easy-to-understand result

🔗 Live Streamlit App:
[Add your Streamlit link here]

🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn
Power BI
Streamlit
Joblib / Pickle
GitHub
📁 Project Structure
Telco-Customer-Churn/
│
├── data/
│   └── telco_customer_churn.csv
│
├── model/
│   └── churn_model.pkl
│
├── app.py
├── requirements.txt
├── README.md
└── PowerBI/
    └── Telco_Customer_Churn.pbix
💡 Key Outcome

This project demonstrates a complete Data Analytics + Machine Learning pipeline, starting from raw customer data and ending with an interactive deployed prediction application.

It combines business intelligence through Power BI with predictive analytics through Machine Learning to support better customer retention decisions.

👩‍💻 Created By

Eng. Habiba Ahmed Talat
Artificial Intelligence Student | Data Analysis & Machine Learning

🔗 Streamlit App: [https://txdtvfy3auggwjzd8g5iqb.streamlit.app/]
