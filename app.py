import streamlit as st 
import pandas as pd 
import pickle
st.set_page_config(page_title='Loan Predictor')
st.header('Welcome to Loan Predictor App')
df=pd.read_csv('cleaned_str.csv')
objects={}
for i in df.columns:
    if df[i].dtype==object:
        objects[i]=list(df[i].unique())
        objects[i].sort()
with open('rfmodel.pkl','rb') as file:
    rfmodel=pickle.load(file)
with st.container(border=True):
    age=st.number_input('Age:',min_value=18,max_value=90)
    gender=st.selectbox('Gender:',options=objects['person_gender'])
    education=st.selectbox('Education:',options=objects['person_education'])
    income=st.number_input('Income:')
    experience=st.number_input('Employee Experience:')
    ownership=st.selectbox('Home Ownership',options=objects['person_home_ownership'])
    loan_amount=st.number_input('Loan Amount:')
    loan_intent=st.selectbox('Loan Intent:',options=objects['loan_intent'])
    loan_int_rate=st.number_input('Loan Initial Rate:')
    loan_percent_income=st.number_input('Loan Percent Income:')
    cb_person_cred_hist_length=st.number_input('Credit History:')
    credit_score=st.number_input('Credit Score:')
    previous_loan_defaults_on_file=st.selectbox('Previous Loan',options=objects['previous_loan_defaults_on_file'])
    input_vals=[[age,objects['person_gender'].index(gender),objects['person_education'].index(education),income,experience,objects['person_home_ownership'].index(ownership),\
                 loan_amount,objects['loan_intent'].index(loan_intent),loan_int_rate,loan_percent_income,cb_person_cred_hist_length,credit_score,objects['previous_loan_defaults_on_file'].index(previous_loan_defaults_on_file)]]
    c1,c2,c3=st.columns([1.8,1.5,1])
    if c2.button('Submit'):
        out=rfmodel.predict(input_vals)
        if out[0]==1:
            st.subheader('Loan can be sanctioned')
        else:
            st.subheader('Loan can not be sanctioned')