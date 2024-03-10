import streamlit as st
import pandas as pd
import joblib
import numpy as np
import time


encoded_data = pd.read_csv('encoded_data.csv')
model = joblib.load('MODEL_RFR.pkl')

job_category = encoded_data.filter(like='category').columns.tolist()
job_title = encoded_data.filter(like='job_title').columns.tolist()
employee_residence = encoded_data.filter(like='employee_residence').columns.tolist()
experience_level = encoded_data.filter(like='experience_level').columns.tolist()
employment_type = encoded_data.filter(like='employment_type').columns.tolist()
work_setting = encoded_data.filter(like='work_setting').columns.tolist()
company_location = encoded_data.filter(like='company_location').columns.tolist()
company_size = encoded_data.filter(like='Company_size').columns.tolist()
Salary=encoded_data["salary_in_usd"]



def extract_substring(value):
    parts = value.rsplit('_', 1)  
    return parts[-1].strip()  

opt_job_category= [extract_substring(value) for value in job_category]


opt_job_title= [extract_substring(value) for value in job_title]


opt_employee_residence= [extract_substring(value) for value in employee_residence]


opt_experience_level= [extract_substring(value) for value in experience_level]


opt_employment_type= [extract_substring(value) for value in employment_type]


opt_work_setting= [extract_substring(value) for value in work_setting]


opt_company_location= [extract_substring(value) for value in company_location]


opt_company_size= [extract_substring(value) for value in company_size]


def preprocess_input(selected_options):
    input_data = pd.DataFrame([selected_options], columns=['job_title', 'job_category', 'employee_residence', 'experience_level', 'employment_type', 'work_setting', 'company_location', 'Company_size'])
    
    input_data_encoded = pd.get_dummies(input_data)
    
    input_data_encoded = input_data_encoded.reindex(columns=encoded_data.drop(columns=['salary_in_usd']).columns, fill_value=0)
    
    return input_data_encoded



def main():
    
   
    st.set_page_config(
        page_title="Salary Predictor",
        page_icon="money.png",
        layout="wide",
    )    
    st.header("")

    st.markdown("<h4 style='text-align: center;'>Analyzing Trends and Disparities in Jobs and Salaries for Data Scientists and Related Fields.<h4>",unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Yearly Job titles increase.</h3>", unsafe_allow_html=True)

    with open('plot.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    st.components.v1.html(html_content, height=600) 
    st.markdown("<h3 style='text-align: center;'>Predict Your Potential Salary.</h3>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>Get an estimated salary based on your job details.</h5>", unsafe_allow_html=True)


    # Input fields
    job_title = st.selectbox(" Job Title",opt_job_title)
 
    job_category = st.selectbox("Job Category",opt_job_category)
    
    employee_residence = st.selectbox("Employee Residence",opt_employee_residence)
    
    experience_level = st.selectbox("Experience Level",opt_experience_level)
    
    employment_type = st.selectbox("Employment Type",opt_employment_type)
    
    work_setting = st.selectbox("Work Setting",opt_work_setting)
    
    company_location = st.selectbox("Company Location",opt_company_location)
    
    company_size = st.selectbox("Company Size",opt_company_size)

    selected_options = [job_title,job_category,employee_residence,experience_level,employment_type,work_setting,company_location,company_size]
     
    

    

    if st.button("Predict Salary"):
        
        progress_bar = st.progress(0)  

        with st.spinner("Making prediction..."):
            input_data = preprocess_input(selected_options)

            for i in range(5):  
                time.sleep(0.5)  
                progress_bar.progress(i / 4) 

                prediction = model.predict(input_data)

            rounded_prediction = np.ceil(prediction[0])
            formatted_salary = format_salary(rounded_prediction)

        st.success(f"Estimated Salary: {formatted_salary}")



    

def format_salary(salary):
    if len(str(salary)) >= 5:
        return f"$ {salary/1000:.0f} k"
    else:
        return f"{salary:.0f}"
    
if __name__ == "__main__":
    main()