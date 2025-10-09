import streamlit as st

st.set_page_config(
    page_title="Churn Prediction App",
    page_icon="📊",
    layout="wide"
)
# ---------------------------------------------------------------
# Landing Section
# ---------------------------------------------------------------
st.title("📈 Customer Churn Prediction System")

st.write("""
Welcome to the *Customer Churn Prediction App*, an interactive web-based system 
developed to help telecom companies identify customers who are likely to discontinue their services.

This system uses *machine learning algorithms* to analyze customer data, 
understand churn patterns, and provide valuable insights that can improve 
customer retention and reduce business losses.
""")

st.markdown("---")

# ---------------------------------------------------------------
# Information Section
# ---------------------------------------------------------------
st.header("🔍 About the Project")

st.write("""
*Customer churn* occurs when customers stop using a company’s services.  
For telecom and subscription-based companies, predicting churn is essential 
for improving customer satisfaction, maintaining loyalty, and ensuring profitability.

This project focuses on:
- Analyzing *historical customer data*
- Identifying *key factors* that lead to churn
- Providing *predictive insights* for proactive decision-making
""")

st.markdown("---")

# ---------------------------------------------------------------
# Technical Overview
# ---------------------------------------------------------------
st.header("⚙ How It Works")

st.write("""
The *Customer Churn Prediction System* performs the following steps:

1. *Data Preprocessing:* Cleans, formats, and prepares the raw customer dataset.  
2. *Exploratory Data Analysis (EDA):* Examines data patterns, correlations, and churn rates.  
3. *Model Training:* Trains various machine learning models such as:
   - Logistic Regression  
   - Random Forest Classifier  
   - AdaBoost Classifier  
4. *Prediction:* Predicts the likelihood of churn based on customer attributes.

These models are trained on key parameters such as:
- Customer demographics (Gender, Age, etc.)  
- Account details (Tenure, Contract Type, Internet Service)  
- Payment and billing information (Monthly & Total Charges)  
""")

st.markdown("---")

# ---------------------------------------------------------------
# Key Features
# ---------------------------------------------------------------
st.header("🚀 Key Features")

st.write("""
- 🧹 *Automated Data Cleaning:* Handles missing values and inconsistent entries.  
- 📊 *Data Visualization:* Shows insights on churn rates and customer patterns.  
- 🤖 *Machine Learning Integration:* Uses multiple algorithms for accuracy.  
- 🧠 *Predictive Analysis:* Estimates churn probability for individual customers.  
- 💾 *Data Storage:* Saves previous results for analysis and review.  
""")

st.markdown("---")

# ---------------------------------------------------------------
# Closing Section
# ---------------------------------------------------------------
st.header("💡 Conclusion")

st.write("""
The *Customer Churn Prediction App* is a complete solution for understanding customer behavior 
and predicting churn using advanced analytics and machine learning.  
It empowers organizations to take *data-driven actions*, reduce customer loss, 
and enhance overall business performance.
""")

st.markdown("---")