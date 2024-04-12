import joblib
import streamlit as st
import pandas as pd

country_mapping = {
    '1. Kenya': 0,
    '2. ReadiRwandang': 1,
    '3. Tanzania': 2,
    '4. Uganda': 3
}

year_mapping = {
    '1. 2016': 0,
    '2. 2017': 1,
    '3. 2018': 2
}

location_mapping = {
    '1. Rural': 0,
    '2. Urban': 1,
}

cellphone_mapping = {
    '1. False': 0,
    '2. True': 1,
}

gender_mapping = {
    '1. Female': 0,
    '2. Male': 1,
}

relationship_mapping = {
    '1. Head of Household': 1,
    '2. Spouse': 5,
    '3. Child': 0,
    '4. Parent': 4, 
    '5. Other Relative': 3,
    '6. Other non-relatives':  2
}

marital_mapping = {
    '1. Married/Living together': 2,
    '2. Widowed': 4,
    '3. Single/Never Married': 3,
    '4. Divorced/Seperated': 0, 
    '5. Dont know ': 1
}

education_mapping = {
    '1. No formal education': 0,
    '2. Primary education': 2,
    '3. Secondary education': 3,
    '4. Tertiary education': 4, 
    '5. Vocational/Specialised training ': 5,
    '6. Other/Dont know/RTA': 1
}

job_mapping = {
    '1. Dont Know/Refuse to answer': 0,
    '2. Farming and Fishing': 1,
    '3. Formally employed Government': 2,
    '4. Formally employed Private': 3,
    '5. Government Dependent': 4, 
    '6. Informally employed': 5,
    '7. No Income':  6,
    '8. Other Income': 7,
    '9. Remittance Dependent': 8,
    '10.  Self employed': 9
}

def convert_to_label(prediction):
    if prediction == 1:
        return "Yes"
    else:
        return "No"

# Load the trained model
loaded_model = joblib.load('model2.pkl')

# Read the dataset
df = pd.read_csv('Financial_inclusion_dataset.csv')

# Drop the 'user_id' column
df.drop(columns=['uniqueid'], inplace=True)

st.title("Checkpoint 29: Streamlit checkpoint 2")
st.subheader("Predicting Churn from Expresso Churn Dataset")
st.text("Please insert your data:")

selected_country = st.selectbox("Country: ", list(country_mapping.keys()))
country= country_mapping[selected_country]
selected_year = st.selectbox("Year: ", list(year_mapping.keys()))
year = year_mapping[selected_year]  # Use year_mapping here
selected_location = st.selectbox("Location Type: ", list(location_mapping.keys()))
location_type = location_mapping[selected_location]
selected_cellphone_access = st.selectbox("Cellphone Access:", list(cellphone_mapping.keys()))
cellphone_access = cellphone_mapping[selected_cellphone_access]
household_size = st.number_input('Household Size')
age_of_respondent = st.number_input('Age of Respondent')
selected_gender = st.selectbox("Gender:", list(gender_mapping.keys()))
gender_of_respondent = gender_mapping[selected_gender]
selected_relationship = st.selectbox("Relationship with Head:", list(relationship_mapping.keys()))
relationship_with_head = relationship_mapping[selected_relationship]
selected_marital = st.selectbox("Marital Status:", list(marital_mapping.keys()))
marital_status = marital_mapping[selected_marital]
selected_education = st.selectbox("Education Level:", list(education_mapping.keys()))
education_level = education_mapping[selected_education]
selected_job = st.selectbox("Job Type:", list(job_mapping.keys()))
job_type = job_mapping[selected_job]

if st.button('Predict'):
    # Create input data for prediction
    input_data = [[country, year, location_type, cellphone_access, household_size, 
                   age_of_respondent, gender_of_respondent, relationship_with_head, 
                   marital_status, education_level, job_type]]
    prediction = loaded_model.predict(input_data)
    predicted_label = convert_to_label(prediction[0])
    st.write('Predicted Bank Account Status:', predicted_label)
    print("Predictions:", predicted_label)
    print("Actual Bank Account Status:", df['bank_account'])