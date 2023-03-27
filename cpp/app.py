import streamlit as st
import pickle
import pandas as pd

cars = pickle.load(open('LinearRegressionModel.pkl','rb'))
car = pd.read_csv('Cleaned Car.csv')



st.title('Car Price Predictor')



carname = st.selectbox(
    'Enter Carname',
    sorted(car['name'].unique()))
carcompany = st.selectbox(
    'Enter Company',
    car['company'].unique())
caryear = st.selectbox(
    'Enter Year',
    sorted(car['year'].unique()))
carfuel = st.selectbox(
    'Enter Fuel Type',
    sorted(car['fuel_type'].unique()))
carkms = st.slider('Kilometres Driven?', 0, 450000, 250000)



predicted_value = cars.predict(pd.DataFrame([[carname,carcompany,caryear,carkms,carfuel]],columns=['name','company','year','kms_driven','fuel_type']))


if st.button('Predict'):
    st.info(f"Predicted Valuation of the car is: *{int(round(predicted_value[0],-2))}*")
