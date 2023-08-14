import streamlit as st
import pandas as pd
import joblib
import numpy as np


st.title('LOAN RISK PREDICTION')
st.write("""
Created by Ridhwan Muttaqien - HCK06


         
Use the sidebar to input customer data.
""")
@st.cache_data
def fetch_data():
    df = pd.read_csv('df_model.csv')
    return df

df = fetch_data()

Income = st.number_input('Income', 0.0)
Age = st.number_input('Age', 0.0)
Experience = st.number_input('Experience', 0.0)
Married_Single = st.selectbox('Marital Status', df['Married/Single'].unique())
House_Ownership = st.selectbox('House Ownership', df['House_Ownership'].unique())
Car_Ownership = st.selectbox('Car Ownership', df['Car_Ownership'].unique())
Profession = st.selectbox('Profession', df['Profession'].unique())
Current_Job_Years = st.number_input('Current Job Years', 0.0)
Current_House_Years = st.number_input('Current House Years', 0.0)

data = {
    'Income': Income,
    'Age': Age,
    'Experience': Experience,
    'Marital Status': Married_Single,
    'House Ownership': House_Ownership,
    'Car Ownership': Car_Ownership,
    'Profession': Profession,
    'Current Job Years': Current_Job_Years,
    'Current House Years' : Current_House_Years
}
input = pd.DataFrame(data, index=[0])



st.subheader('Customer Data')
st.write(input)

load_model = joblib.load("loanrisk_pred.pkl")

if st.button('Predict'):
    prediction = load_model.predict(input)

    if prediction == 1:
        prediction = 'Risky Loan'
    else:
        prediction = 'Not Risky Loan'

    st.write('Based on Customer Data, the loan predicted: ')
    st.write(prediction)