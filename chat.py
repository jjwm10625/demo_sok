import streamlit as st
import pandas as pd
import plotly.express as px

# CSV 파일 읽기
titanic_data = pd.read_csv('titanic.csv')

# 성별과 생존 유무에 따라 그룹화
grouped_data = titanic_data.groupby(['Sex', 'Survived']).size().unstack().reset_index()

# Streamlit App
st.title('Survival Status by Gender')

# Display the raw data
st.subheader('Raw Data')
st.write(grouped_data)

# Plot using Plotly Express
fig = px.bar(grouped_data, x='Sex', y=[0, 1], color_discrete_map={0: 'red', 1: 'green'},
             labels={'Sex': 'Gender', '0': 'Not Survived', '1': 'Survived'},
             title='Survival Status by Gender',
             barmode='stack')

# Show the Plotly figure in the Streamlit app
st.plotly_chart(fig)
