import streamlit as st
import pandas as pd

st. set_page_config(layout="wide") 

df = pd.read_csv("diabetes_prediction_dataset.csv")

st.write(df.columns)
