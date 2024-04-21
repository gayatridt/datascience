import streamlit as st
import pandas as pd
import io

st. set_page_config(layout="wide") 

df = pd.read_csv("diabetes_prediction_dataset.csv")

st.subheader('Columns in Dataset:')
st.write(df.columns)

st.subheader('Shape of Dataset:')
st.write(df.shape)

st.subheader('Concise summary of the Dataset:')
buffer = io.StringIO()
df.info(buf=buffer)
sInfo = buffer.getvalue()
st.text(sInfo)

st.subheader('Statistics for Numerical columns')
st.write(df.describe())
