import streamlit as st
import requests

job_title = [
    "AI Architect",
    "AI Developer",
    "AI Engineer",
    "AI Programmer",
    "AI Research Engineer",
    "AI Scientist",
    "Analytics Engineer",
    "Analytics Engineering Manager",
    "Applied Data Scientist",
    "Applied Machine Learning Engineer",
    "Applied Machine Learning Scientist",
    "Applied Scientist",
    "Autonomous Vehicle Technician",
    "AWS Data Architect",
    "Azure Data Engineer",
    "BI Analyst",
    "BI Data Analyst",
    "BI Data Engineer",
    "BI Developer",
    "Big Data Architect",
    "Big Data Engineer",
    "Business Data Analyst",
    "Business Intelligence Analyst",
    "Business Intelligence Data Analyst",
    "Business Intelligence Developer",
    "Business Intelligence Engineer",
    "Business Intelligence Manager",
    "Business Intelligence Specialist",
    "Cloud Data Architect",
    "Cloud Data Engineer",
    "Cloud Database Engineer",
    "Compliance Data Analyst",
    "Computer Vision Engineer",
    "Computer Vision Software Engineer",
    "Data Analyst",
    "Data Analytics Consultant",
    "Data Analytics Engineer",
    "Data Analytics Lead",
    "Data Analytics Manager",
    "Data Analytics Specialist",
    "Data Architect",
    "Data Developer",
    "Data Engineer",
    "Data Infrastructure Engineer",
    "Data Integration Engineer",
    "Data Integration Specialist",
    "Data Lead",
    "Data Management Analyst",
    "Data Management Specialist",
    "Data Manager",
    "Data Modeller",
    "Data Modeler",
    "Data Operations Analyst",
    "Data Operations Engineer",
    "Data Operations Manager",
    "Data Operations Specialist",
    "Data Product Manager",
    "Data Product Owner",
    "Data Quality Analyst",
    "Data Quality Engineer",
    "Data Science Consultant",
    "Data Science Director",
    "Data Science Engineer",
    "Data Science Lead",
    "Data Science Manager",
    "Data Science Practitioner",
    "Data Scientist",
    "Data Scientist Lead",
    "Data Specialist",
    "Data Strategist",
    "Data Strategy Manager",
    "Decision Scientist",
    "Deep Learning Engineer",
    "Deep Learning Researcher",
    "Director of Data Science",
    "ETL Developer",
    "ETL Engineer",
    "Finance Data Analyst",
    "Financial Data Analyst",
    "Head of Data",
    "Head of Data Science",
    "Head of Machine Learning",
    "Insight Analyst",
    "Lead Data Analyst",
    "Lead Data Engineer",
    "Lead Machine Learning Engineer",
    "Lead Data Scientist",
    "Machine Learning Developer",
    "Machine Learning Engineer",
    "Machine Learning Infrastructure Engineer",
    "Machine Learning Manager",
    "Machine Learning Modeler",
    "Machine Learning Operations Engineer",
    "Machine Learning Research Engineer",
    "Machine Learning Researcher",
    "Machine Learning Scientist",
    "Machine Learning Software Engineer",
    "Machine Learning Specialist",
    "Manager Data Management",
    "Managing Director Data Science",
    "Marketing Data Analyst",
    "Marketing Data Engineer",
    "NLP Engineer",
    "Power BI Developer",
    "Principal Data Analyst",
    "Principal Data Engineer",
    "Principal Data Scientist",
    "Principal Machine Learning Engineer",
    "Product Data Analyst",
    "Research Analyst",
    "Research Engineer",
    "Research Scientist",
    "Sales Data Analyst",
    "Software Data Engineer",
    "Staff Data Analyst",
    "Staff Data Scientist",
    "Staff Machine Learning Engineer",
    "Streamlit",
    "Consultant Data Engineer"
]

job_category = [
    "BI and Visualization", "Cloud and Database", "Data Analysis", "Data Architecture and Modeling",
    "Data Engineering", "Data Management and Strategy", "Data Quality and Operations", "Data Science and Research",
    "Leadership and Management", "Machine Learning and AI"
]

employee_residence = [
    "Algeria", "American Samoa", "Andorra", "Argentina", "Armenia", "Australia", "Austria", "Belgium", "Bolivia",
    "Bosnia and Herzegovina", "Brazil", "Bulgaria", "Canada", "Central African Republic", "Chile", "China", "Colombia",
    "Costa Rica", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Dominican Republic", "Ecuador", "Egypt", "Estonia",
    "Finland", "France", "Georgia", "Germany", "Ghana", "Greece", "Hong Kong", "Honduras", "India", "Indonesia", "Iran",
    "Iraq", "Ireland", "Italy", "Japan", "Jersey", "Kenya", "Kuwait", "Latvia", "Lithuania", "Luxembourg", "Malaysia",
    "Malta", "Mauritius", "Mexico", "Moldova", "Netherlands", "New Zealand", "Nigeria", "Pakistan", "Peru", "Philippines",
    "Poland", "Portugal", "Puerto Rico", "Qatar", "Romania", "Russia", "Saudi Arabia", "Serbia", "Singapore", "Slovenia",
    "South Africa", "South Korea", "Spain", "Sweden", "Switzerland", "Thailand", "Tunisia", "Turkey", "Uganda", "Ukraine",
    "United Arab Emirates", "United Kingdom", "United States", "Uzbekistan", "Vietnam"
]

experience_level = ["Senior", "Mid-level", "Executive", "Entry-level"]

employment_type = ["Full-time", "Part-time", "Contract", "Freelance"]

work_setting = ["Hybrid", "In-person", "Remote"]

company_location = [
    "Algeria", "American Samoa", "Andorra", "Argentina", "Armenia", "Australia", "Austria", "Belgium", "Bolivia",
    "Bosnia and Herzegovina", "Brazil", "Bulgaria", "Canada", "Central African Republic", "Chile", "China", "Colombia",
    "Costa Rica", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Dominican Republic", "Ecuador", "Egypt", "Estonia",
    "Finland", "France", "Georgia", "Germany", "Ghana", "Greece", "Hong Kong", "Honduras", "India", "Indonesia", "Iran",
    "Iraq", "Ireland", "Italy", "Japan", "Jersey", "Kenya", "Kuwait", "Latvia", "Lithuania", "Luxembourg", "Malaysia",
    "Malta", "Mauritius", "Mexico", "Moldova", "Netherlands", "New Zealand", "Nigeria", "Pakistan", "Peru", "Philippines",
    "Poland", "Portugal", "Puerto Rico", "Qatar", "Romania", "Russia", "Saudi Arabia", "Serbia", "Singapore", "Slovenia",
    "South Africa", "South Korea", "Spain", "Sweden", "Switzerland", "Thailand", "Tunisia", "Turkey", "Uganda", "Ukraine",
    "United Arab Emirates", "United Kingdom", "United States", "Uzbekistan", "Vietnam"
]

company_size = ["Small","Medium","Large"]

@st.cache(allow_output_mutation=True)
def predict_salary(data):
    url = "http://127.0.0.1:8000/predict_salary"
    response = requests.post(url, json=data)
    prediction = response.json()
    return prediction["predicted_salary"]

st.title("SALARY PREDICTION")

st.subheader("SELECT SUITABLE OPTIONS")
job_title_input = st.selectbox("Job Title", job_title)
job_category_input = st.selectbox("Job Category", job_category)
employee_residence_input = st.selectbox("Employee Residence", employee_residence)
experience_level_input = st.selectbox("Experience Level", experience_level)
employment_type_input = st.selectbox("Employment Type", employment_type)
work_setting_input = st.selectbox("Work Setting", work_setting)
company_location_input = st.selectbox("Company Location", company_location)
company_size_input = st.selectbox("Company Size", company_size)

data = {
    "job_title": job_title_input,
    "job_category": job_category_input,
    "employee_residence": employee_residence_input,
    "experience_level": experience_level_input,
    "employment_type": employment_type_input,
    "work_setting": work_setting_input,
    "company_location": company_location_input,
    "company_size": company_size_input
}


DATA=[    'Company_size_Large', 'Company_size_Medium', 'Company_size_Small', 'company_location_Algeria', 
    'company_location_American Samoa', 'company_location_Andorra', 'company_location_Argentina', 
    'company_location_Armenia', 'company_location_Australia', 'company_location_Austria', 'company_location_Bahamas', 
    'company_location_Belgium', 'company_location_Bosnia and Herzegovina', 'company_location_Brazil', 
    'company_location_Canada', 'company_location_Central African Republic', 'company_location_China', 
    'company_location_Colombia', 'company_location_Croatia', 'company_location_Czech Republic', 
    'company_location_Denmark', 'company_location_Ecuador', 'company_location_Egypt', 'company_location_Estonia', 
    'company_location_Finland', 'company_location_France', 'company_location_Germany', 'company_location_Ghana', 
    'company_location_Gibraltar', 'company_location_Greece', 'company_location_Honduras', 'company_location_India', 
    'company_location_Indonesia', 'company_location_Iran', 'company_location_Iraq', 'company_location_Ireland', 
    'company_location_Israel', 'company_location_Italy', 'company_location_Japan', 'company_location_Kenya', 
    'company_location_Latvia', 'company_location_Lithuania', 'company_location_Luxembourg', 'company_location_Malaysia', 
    'company_location_Malta', 'company_location_Mauritius', 'company_location_Mexico', 'company_location_Moldova', 
    'company_location_Netherlands', 'company_location_New Zealand', 'company_location_Nigeria', 'company_location_Pakistan', 
    'company_location_Philippines', 'company_location_Poland', 'company_location_Portugal', 'company_location_Puerto Rico', 
    'company_location_Qatar', 'company_location_Romania', 'company_location_Russia', 'company_location_Saudi Arabia', 
    'company_location_Singapore', 'company_location_Slovenia', 'company_location_South Africa', 'company_location_South Korea', 
    'company_location_Spain', 'company_location_Sweden', 'company_location_Switzerland', 'company_location_Thailand', 
    'company_location_Turkey', 'company_location_Ukraine', 'company_location_United Arab Emirates', 'company_location_United Kingdom', 
    'company_location_United States', 'employee_residence_Algeria', 'employee_residence_American Samoa', 'employee_residence_Andorra', 
    'employee_residence_Argentina', 'employee_residence_Armenia', 'employee_residence_Australia', 'employee_residence_Austria', 
    'employee_residence_Belgium', 'employee_residence_Bolivia', 'employee_residence_Bosnia and Herzegovina', 'employee_residence_Brazil', 
    'employee_residence_Bulgaria', 'employee_residence_Canada', 'employee_residence_Central African Republic', 'employee_residence_Chile', 
    'employee_residence_China', 'employee_residence_Colombia', 'employee_residence_Costa Rica', 'employee_residence_Croatia', 
    'employee_residence_Cyprus', 'employee_residence_Czech Republic', 'employee_residence_Denmark', 'employee_residence_Dominican Republic', 
    'employee_residence_Ecuador', 'employee_residence_Egypt', 'employee_residence_Estonia', 'employee_residence_Finland', 
    'employee_residence_France', 'employee_residence_Georgia', 'employee_residence_Germany', 'employee_residence_Ghana', 
    'employee_residence_Greece', 'employee_residence_Honduras', 'employee_residence_Hong Kong', 'employee_residence_India', 
    'employee_residence_Indonesia', 'employee_residence_Iran', 'employee_residence_Iraq', 'employee_residence_Ireland', 
    'employee_residence_Italy', 'employee_residence_Japan', 'employee_residence_Jersey', 'employee_residence_Kenya', 
    'employee_residence_Kuwait', 'employee_residence_Latvia', 'employee_residence_Lithuania', 'employee_residence_Luxembourg', 
    'employee_residence_Malaysia', 'employee_residence_Malta', 'employee_residence_Mauritius', 'employee_residence_Mexico', 
    'employee_residence_Moldova', 'employee_residence_Netherlands', 'employee_residence_New Zealand', 'employee_residence_Nigeria', 
    'employee_residence_Pakistan', 'employee_residence_Peru', 'employee_residence_Philippines', 'employee_residence_Poland', 
    'employee_residence_Portugal', 'employee_residence_Puerto Rico', 'employee_residence_Qatar', 'employee_residence_Romania', 
    'employee_residence_Russia', 'employee_residence_Saudi Arabia', 'employee_residence_Serbia', 'employee_residence_Singapore', 
    'employee_residence_Slovenia', 'employee_residence_South Africa', 'employee_residence_South Korea', 'employee_residence_Spain', 
    'employee_residence_Sweden', 'employee_residence_Switzerland', 'employee_residence_Thailand', 'employee_residence_Tunisia', 
    'employee_residence_Turkey', 'employee_residence_Uganda', 'employee_residence_Ukraine', 'employee_residence_United Arab Emirates', 
    'employee_residence_United Kingdom', 'employee_residence_United States', 'employee_residence_Uzbekistan', 'employee_residence_Vietnam', 
    'employment_type_Contract', 'employment_type_Freelance', 'employment_type_Full-time', 'employment_type_Part-time', 
    'experience_level_Entry-level', 'experience_level_Executive', 'experience_level_Mid-level', 'experience_level_Senior', 
    'job_category_BI and Visualization', 'job_category_Cloud and Database', 'job_category_Data Analysis', 'job_category_Data Architecture and Modeling', 
    'job_category_Data Engineering', 'job_category_Data Management and Strategy', 'job_category_Data Quality and Operations', 
    'job_category_Data Science and Research', 'job_category_Leadership and Management', 'job_category_Machine Learning and AI', 
    'job_title_AI Architect', 'job_title_AI Developer', 'job_title_AI Engineer', 'job_title_AI Programmer', 'job_title_AI Research Engineer', 
    'job_title_AI Scientist', 'job_title_AWS Data Architect', 'job_title_Analytics Engineer', 'job_title_Analytics Engineering Manager', 
    'job_title_Applied Data Scientist', 'job_title_Applied Machine Learning Engineer', 'job_title_Applied Machine Learning Scientist', 
    'job_title_Applied Scientist', 'job_title_Autonomous Vehicle Technician', 'job_title_Azure Data Engineer', 'job_title_BI Analyst', 
    'job_title_BI Data Analyst', 'job_title_BI Data Engineer', 'job_title_BI Developer', 'job_title_Big Data Architect'

]

if st.button("Predict Salary"):
    predicted_salary = predict_salary(data)
    st.success(f"Predicted Salary: {predicted_salary}")
