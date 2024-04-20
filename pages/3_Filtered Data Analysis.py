import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import numpy as np

# Load the dataset
@st.cache(allow_output_mutation=True)
def load_data():
    return pd.read_csv("diabetes_prediction_dataset.csv")

data = load_data()

# Filter data based on user input
st.title("Filter Data")

selected_gender = st.multiselect("Select Gender", data["gender"].unique())
selected_age = st.slider("Select Age Range", int(data["age"].min()), int(data["age"].max()), (0, 100))
selected_hypertension = st.selectbox("Hypertension", ["All"] + list(data["hypertension"].unique()))
selected_heart_disease = st.selectbox("Heart Disease", ["All"] + list(data["heart_disease"].unique()))
selected_smoking_history = st.multiselect("Smoking History", data["smoking_history"].unique())
selected_diabetes = st.selectbox("Diabetes", ["All"] + list(data["diabetes"].unique()))

# Search button
search_button = st.button("Search")

# Clear button
clear_button = st.button("Clear Filters")

if clear_button:
     # Reset filters
    selected_gender = ["Male", "Female", "Other"]
    selected_smoking_history = ["Unknown", "Never Smoked", "Formerly Smoked", "Smokes"]
    selected_age = (int(data["age"].min()), int(data["age"].max()))
    selected_hypertension = "All"
    selected_heart_disease = "All"
    selected_diabetes = "All"

if search_button:
    # Apply filters
    filtered_data = data[
        (data["gender"].isin(selected_gender)) &
        (data["age"].between(selected_age[0], selected_age[1])) &
        ((selected_hypertension == "All") | (data["hypertension"] == selected_hypertension)) &
        ((selected_heart_disease == "All") | (data["heart_disease"] == selected_heart_disease)) &
        (data["smoking_history"].isin(selected_smoking_history)) &
        ((selected_diabetes == "All") | (data["diabetes"] == selected_diabetes))
    ]

    # Display filtered data
    st.write("## Filtered Data")
    st.write(filtered_data)

    # Summary Statistics
    st.write("## Summary Statistics")
    st.write(filtered_data.describe())

    # Histograms
    st.write("## Histograms")
    numeric_columns = ["age", "bmi", "HbA1c_level", "blood_glucose_level"]
    for col in numeric_columns:
        fig = px.histogram(filtered_data, x=col, title=f"{col.capitalize()} Distribution")
        st.plotly_chart(fig)

    # Pair plot
    st.write("## Pair Plot")
    fig_pair = px.scatter_matrix(filtered_data.drop(columns=["gender"]).select_dtypes(include=[np.number]), dimensions=numeric_columns, height=1000, width=1000)
    st.plotly_chart(fig_pair)

    # Heatmap
    st.write("## Heatmap")
    corr = filtered_data.select_dtypes(include=[np.number]).corr().round(2)  # Round the correlation values to two decimal places
    fig_heatmap = ff.create_annotated_heatmap(z=corr.values,
                                              x=list(corr.index),
                                              y=list(corr.columns),
                                              colorscale='Viridis')
    fig_heatmap.update_layout(title="Correlation Heatmap", height=800, width=800)
    st.plotly_chart(fig_heatmap)
