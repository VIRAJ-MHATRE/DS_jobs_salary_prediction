import streamlit as st
import pandas as pd
import joblib

# Replace with your actual paths
encoded_data = pd.read_csv('encoded_data.csv')
model = joblib.load('MODEL_RFR.pkl')

# Get feature names used during training (assuming this is stored in a variable)
trained_features = model.feature_names_in_

def preprocess_input(selected_options):
  # Create a DataFrame with selected options
  input_data = pd.DataFrame(selected_options, columns=['selected_options'])

  # One-hot encode the input data
  input_data_encoded = pd.get_dummies(input_data)

  # Ensure consistent feature names with training
  missing_features = set(trained_features) - set(input_data_encoded.columns)
  if missing_features:
      # Add missing features with zero values (assuming this aligns with training)
      for feature in missing_features:
          input_data_encoded[feature] = 0
  
  # Reindex to match the columns used during training
  input_data_encoded = input_data_encoded.reindex(columns=trained_features, fill_value=0)
  
  return input_data_encoded



def main():
  st.title("Salary Prediction")

  # Input fields (assuming these match trained features)
  job_title = st.selectbox("Job Title",encoded_data.filter(like='job_title').columns.tolist())
  st.write("You selected:", job_title)
  
  job_category = st.selectbox("Job Category",encoded_data.filter(like='category').columns.tolist())
  st.write("You selected:", job_category)
  
  employee_residence = st.selectbox("Employee Residence",encoded_data.filter(like='employee_residence').columns.tolist())
  st.write("You selected:", employee_residence)
  
  experience_level = st.selectbox("Experience Level",encoded_data.filter(like='experience_level').columns.tolist())
  st.write("You selected:", experience_level)
  
  employment_type = st.selectbox("Employment Type",encoded_data.filter(like='employment_type').columns.tolist())
  st.write("You selected:", employment_type)
  
  work_setting = st.selectbox("Work Setting",encoded_data.filter(like='work_setting').columns.tolist())
  st.write("You selected:", work_setting)
  
  company_location = st.selectbox("Company Location",encoded_data.filter(like='company_location').columns.tolist())
  st.write("You selected:", company_location)
  
  company_size = st.selectbox("Company Size",encoded_data.filter(like='Company_size').columns.tolist())
  st.write("You selected:", company_size)

  selected_options = [job_title,job_category,employee_residence,experience_level,employment_type,work_setting,company_location,company_size]
  
  if st.button("Predict Salary"):
    # Preprocess input data
    input_data = preprocess_input(selected_options)
    
    prediction = model.predict(input_data)
    
    # Display prediction
    st.success(f"Predicted Salary (in USD): {prediction[0]}")


if __name__ == "__main__":
  main()
