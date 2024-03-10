import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import OneHotEncoder

# Load the trained model
model = joblib.load("MODEL_RFR.pkl")

# Load the encoded data
encoded_data = pd.read_csv("encoded_data.csv")

# Function to preprocess input data
def preprocess_input(job_title, job_category, employee_residence, experience_level, employment_type, work_setting, company_location, company_size):
    # Create a DataFrame with input data
    input_data = pd.DataFrame({
        'job_title': [job_title],
        'job_category': [job_category],
        'employee_residence': [employee_residence],
        'experience_level': [experience_level],
        'employment_type': [employment_type],
        'work_setting': [work_setting],
        'company_location': [company_location],
        'Company_size': [company_size]
    })

    # One-hot encode the input data
    input_data_encoded = pd.get_dummies(input_data)
    input_data_encoded = input_data_encoded.reindex(columns=encoded_data.columns, fill_value=0)

    return input_data_encoded

job_category = encoded_data.filter(like='category').columns.tolist()
job_title = encoded_data.filter(like='job_title').columns.tolist()
employee_residence = encoded_data.filter(like='employee_residence').columns.tolist()
experience_level = encoded_data.filter(like='experience_level').columns.tolist()
employment_type = encoded_data.filter(like='employment_type').columns.tolist()
work_setting = encoded_data.filter(like='work_setting').columns.tolist()
company_location = encoded_data.filter(like='company_location').columns.tolist()
company_size = encoded_data.filter(like='company_size').columns.tolist()

# Streamlit app
def main():
    st.title("Salary Prediction")

    # Input fields
    job_title = st.text_input("Job Title")
    job_category = st.text_input("Job Category")
    employee_residence = st.text_input("Employee Residence")
    experience_level = st.text_input("Experience Level")
    employment_type = st.text_input("Employment Type")
    work_setting = st.text_input("Work Setting")
    company_location = st.text_input("Company Location")
    company_size = st.text_input("Company Size")

    # Predict button
    if st.button("Predict Salary"):
        # Preprocess input data
        input_data = preprocess_input(job_title, job_category, employee_residence, experience_level, employment_type, work_setting, company_location, company_size)

        # Make prediction
        prediction = model.predict(input_data)
        st.success(f"Predicted Salary (in USD): {prediction[0]}")

if __name__ == "__main__":
    main()
