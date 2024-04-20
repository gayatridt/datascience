import streamlit as st
import pandas as pd
from streamlit.logger import get_logger

st. set_page_config(layout="wide") 

LOGGER = get_logger(__name__)

def run():

    st.sidebar.success("Select a menu above.")
    st.title('Data Science Engg. Methods & Tools - Final Project')
    st.header('Diabetes Prediction')
    st.subheader('Report Sumary')

    df = pd.read_csv("diabetes_prediction_dataset.csv")
    st.write(df)

    st.markdown('''The dataset contains 100,000 records with 9 columns. Each row represents an individual patient.
    The columns include:  exit()
                
                
    Gender: Categorical variable indicating the gender of the patient (Male/Female/Other).  
                
    Age: Continuous variable representing the age of the patient.  
                
    Hypertension: Binary variable indicating the presence of hypertension (0: No, 1: Yes).  
                
    Heart Disease: Binary variable indicating the presence of heart disease (0: No, 1: Yes).  
                
    Smoking History: Categorical variable indicating the smoking history of the patient (never/current/former/No Info).  
                
    BMI: Continuous variable representing the Body Mass Index (BMI) of the patient.  
                
    HbA1c Level: Continuous variable representing the HbA1c level of the patient.  
                
    Blood Glucose Level: Continuous variable representing the blood glucose level of the patient.  
                
    Diabetes: Binary variable indicating the presence of diabetes (0: No, 1: Yes).''')

if __name__ == "__main__":
    run()