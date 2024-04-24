import streamlit as st
import pickle
import pandas as pd

# Loading the trained model from the pickle file
model_path = 'trainedfinalmodel.pkl'  
with open(model_path, 'rb') as file:
    trained_model = pickle.load(file)

def app():
    st.set_page_config(page_title="Diabetes Prediction")

    st.title("Diabetes Prediction Tool")
    st.markdown("Use this tool to predict whether a person has diabetes based on various health indicators. Fill in the form below and click 'Predict'.")

    # Input fields
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=0, max_value=120, value=25, help="Enter the age of the person")
        hypertension = st.selectbox("Hypertension", ["No", "Yes"], help="Does the person have hypertension?")
        heart_disease = st.selectbox("Heart Disease", ["No", "Yes"], help="Does the person have heart disease?")
        smoking_history = st.selectbox("Smoking History",
                                       ["Never", "Ever", "Current", "Former", "Not Current", "No Info"],
                                       help="Select the person's smoking history")
        bmi = st.number_input("BMI", min_value=10.0, max_value=100.0, value=25.0, help="Enter the person's BMI")

    with col2:
        hb_a1c_level = st.number_input("HbA1c Level", min_value=3.5, max_value=9.0, value=5.5,
                                       help="Enter the person's HbA1c level")
        blood_glucose_level = st.number_input("Blood Glucose Level", min_value=80, max_value=300, value=100,
                                              help="Enter the person's blood glucose level")
        gender = st.selectbox("Gender", ["Female", "Male", "Other"], help="Select the person's gender")

    # Button for prediction
    if st.button("Predict"):
        input_data = pd.DataFrame({
            "age": [age],
            "hypertension": [1 if hypertension == "Yes" else 0],
            "heart_disease": [1 if heart_disease == "Yes" else 0],
            "smoking_history": [smoking_history],
            "bmi": [bmi],
            "HbA1c_level": [hb_a1c_level],
            "blood_glucose_level": [blood_glucose_level],
            "gender_Female": [1 if gender == "Female" else 0],
            "gender_Male": [1 if gender == "Male" else 0],
            "gender_Other": [1 if gender == "Other" else 0]
        })

        # Mapping smoking history to numerical values
        input_data["smoking_history"] = input_data["smoking_history"].map(
            {'No Info': 0, 'Never': 1, 'Ever': 2, 'Former': 3, 'Not Current': 4, 'Current': 5}
        )

        prediction = trained_model.predict(input_data)

        if prediction == 0:
            st.success("The prediction is: No Diabetes")
        else:
            st.warning("The prediction is: Diabetes")

if __name__ == "__main__":
    app()