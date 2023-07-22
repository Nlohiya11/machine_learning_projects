import pickle
import numpy as np
import streamlit as st
import pandas as pd
ran = [1, 2, 3, 4, 5, 6, 7, 8]
data = pd.read_csv('final_result.csv')
area = data['location'].unique()

st.title("House Price Prediction in Bangalore")

model = pickle.load(open('RidgeModel.pkl', 'rb'))

location = st.selectbox("Select your Location", area)
input_bhk = st.selectbox("Enter Your BHK", ran)
input_bathroom = st.selectbox("Enter how many bathroom it required", ran)
input_area = st.text_input("Enter the total square feet required")


def predict_prize():
    input_ans = pd.DataFrame([[location, input_bhk, input_bathroom, input_area]], columns=['location', 'size', 'bath', 'total_sqft'])
    prediction = model.predict(input_ans)[0] * 100000

    return np.round(prediction, 1)


if st.button('Predict'):
    answer = predict_prize()
    if answer <= 0:
        st.header("There is no such property available")
    else:
        st.header("₹ "+str(answer))
