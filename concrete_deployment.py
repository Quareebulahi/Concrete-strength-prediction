import streamlit as st
import joblib
import pandas as pd
import numpy as np
import pickle
#pipeline = joblib.load('concrete_pipeline.joblib')

with open('my_pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)


def collect_user_input():
    st.title('Concrete Strength Prediction App')
    st.markdown('**Input your concrete composition**')
    cement = st.number_input('Cement', min_value=100, max_value=600, value=100)
    slag = st.number_input('Slag', min_value=0, max_value=400, value=0)
    ash = st.number_input('Ash', min_value=0, max_value=400, value=0)
    water = st.number_input('Water', 100, 400, 100)
    superplastic = st.number_input('Super Plastic', 0, 100, 0)
    coarseagg = st.number_input('Coarse Aggregrate', 0, 2000, 0)
    fineagg = st.number_input('Fine Aggregate', 0, 1000, 0 )
    age = st.number_input('Age', 1, 365, 1)
    user_input = pd.DataFrame([[cement, slag, ash, water, superplastic ,coarseagg, fineagg, age]], columns=[
        'cement', 'slag', 'ash', 'water', 'superplastic', 'coarseagg', 'fineagg', 'age'
    ])
    return user_input

input_data =  collect_user_input()
if st.button('Predict'):
    with st.spinner('Calculating prediction...'):
        prediction = pipeline.predict(input_data)
        result =  np.round(prediction[0], 0)
        st.success(f'Your cement strength is {result} MPa.')
        
