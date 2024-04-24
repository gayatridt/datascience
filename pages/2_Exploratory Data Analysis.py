import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

df = pd.read_csv("diabetes_prediction_dataset.csv")

# Pie charts
st.subheader('Pie Chart')
df_eda = df[['gender', 'hypertension', 'heart_disease', 'smoking_history', 'diabetes']]

for column in df_eda.columns:
    value_counts = df_eda[column].value_counts()
    fig = px.pie(names=value_counts.index, values=value_counts.values, title=f'Pie Chart for {column} Distribution')
    fig.update_traces(textinfo='percent+label')
    st.plotly_chart(fig)

st.subheader('Observations')

st.markdown('''Pie charts are effective for visualizing the distribution of categorical variables. They display the proportion of each category within the dataset, making it easy to identify the most common categories and any imbalances in the data.  
            
Gender: distribution in the dataset is predominantly female, accounting for 58.6% of the individuals. Male individuals make up 41.4% of the dataset, while 0.018% records categorized as other gender.
            
Hypertension: Approximately 92.5% of individuals in the dataset do not have hypertension (labeled as 0). About 7.49% of individuals have hypertension (labeled as 1).  
            
Heart disease: Around 96.1% of individuals in the dataset do not have heart disease (labeled as 0). Approximately 3.94% of individuals have heart disease (labeled as 1).  
            
Smoking history distribution: About 9.29% of individuals are current smokers. Approximately 9.35% of individuals are former smokers. Around 6.45% of individuals have a smoking history but are not current smokers. About 4.0% of individuals have ever smoked. About 35.1% of individuals have never smoked. Approximately 35.8% of individuals have no information available regarding their smoking history.  
            
Diabetes: Approximately 91.5% of individuals in the dataset do not have diabetes (labeled as 0). Around 8.5% of individuals have diabetes (labeled as 1).''')

# Histograms

st.subheader('Histogram')

df_eda_1 = df[['age','bmi','HbA1c_level','blood_glucose_level']]

for column in df_eda_1.columns:
    fig = px.histogram(df_eda_1[column], 
                       title=f'Histogram of {column}', 
                       nbins=10, 
                       opacity=0.7, 
                       barnorm='percent', 
                       barmode='overlay',
                       text_auto=True,
                       labels={'count':'Count', 'percentage':'Percentage'})
    fig.update_traces(marker_line_width=1.5, marker_line_color="black")
    fig.update_layout(showlegend=False, height=600)  # Hide legend to prevent duplication
    st.plotly_chart(fig)

st.subheader('Observations')

st.markdown('''Histogram is providing valuable insights into the distribution of continuious numerical variables with columns such as age,bmi,HbA1c_level and blood_glucose_level.  
            
1.We can come to conclusion that age feature is symmetricial enough with data above and below 40 being equally distributed with multiple modes.  
            
2.BMI feature seems to be left skewed as the the distribution on the left side sees to be more than the right side.  
            
3.HbA1c_Level feature seems to be right skewed with highest mode for 6 range value with 400000 records and furthermore.  
            
4.Blood Glucose also has right skewed data as 30000 having glucode ranges from 100 -150 range and in the consequitive range achieves the second largest modal count with 29000.''')

# Box plots

st.subheader('Box Plot')

df_eda_2 = df.drop(['diabetes', 'hypertension', 'heart_disease', 'gender', 'smoking_history'], axis=1)

for column in df_eda_2.columns:
    fig = px.box(df_eda_2, y=column, title=f"{column.capitalize()} Boxplot")
    st.plotly_chart(fig)

st.subheader('Observations')

st.markdown('''The presence of outliers is maximum for BMI followed by blood_glucose_level , and HbA1c_level whereas age does not have any outliers.''')


