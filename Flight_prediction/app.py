import datetime
import pickle
import numpy as np
import streamlit as st
import pandas as pd
from datetime import datetime

#copying the data to this python file
data = pd.read_csv('final_result.csv')

source = data['source_city'].sort_values(axis=0, ascending=True).unique()
destination = data['destination_city'].sort_values(axis=0, ascending=True).unique()
airlines = data["airline"].sort_values(axis=0, ascending=True).unique()
times = data['departure_time'].sort_values(axis=0, ascending=True).unique()
stops = data['stops'].unique()
class_f = data['class'].sort_values(axis=0, ascending=True).unique()
days = data['days_left'].unique()
current_date = str(datetime.now())
present_date = current_date.split(" ")[0]


def total_days(x):
    date = x.split("-")
    year_1 = int(date[0])
    month_1 = int(date[1])
    day_1 = int(date[2])
    return year_1*365 + month_1*31 + day_1


model = pickle.load(open('Model_flights.pkl', 'rb'))
airline_categoricalCol = ['airline', 'source_city', 'departure_time', 'destination_city', 'class']
dum_df = pd.get_dummies(data, columns=airline_categoricalCol, dtype=int)
dit = dum_df.drop(columns=['price', 'Unnamed: 0'])
cols = dit.columns.values

source_city = st.selectbox("Select your City from which you need to fly :", source)
destination_city = st.selectbox("Select Destination City :", destination)
airline = st.selectbox("Select the Airline you want to choose :", airlines)
col1, col2 = st.columns([3, 1])
time_suggestion = col2.expander("Insights for choosing correct time")
time_suggestion.write(''' Rush Wise-
Most People travel in morning followed by early morning
Least people travel at Late Night
Price Wise-
Night has the most expensive price
Late_Night has the least average price ''')
departure_time = col1.selectbox("Select the Airline you want to choose :", times)
stops_insight = col2.expander("Insights for choosing stops")
stops_insight.write('''On last day flights sell lower price ticket to fill seat.
We should book out ticket earlier to get lower price in ticket.
As day increses the price of ticket goes higher.
if you want higher stops than 2. please specify''')

d = str(st.date_input("When's your birthday"))
days_left = total_days(d) - total_days(present_date)
stop = col1.selectbox("Select class of flight :", stops)
clas = st.selectbox("Select class of flight :", class_f)
duration = st.number_input("Select the average duration for the jurney :")
data_answer = [stop, duration, days_left]


def input_answers(sources, input_source):
    for i in sources:
        if i == input_source:
            data_answer.append(1)
        else:
            data_answer.append(0)


input_answers(airlines, airline)
input_answers(source, source_city)
input_answers(times, departure_time)
input_answers(destination, destination_city)
input_answers(class_f, clas)


def predict_prize():
    input_ans = pd.DataFrame([data_answer], columns=cols)
    prediction = model.predict(input_ans)[0]
    return np.round(prediction, 1)


if st.button('Predict'):
    answer = predict_prize()
    if answer <= 0:
        st.header("There is no such Flight available")
    else:
        st.header("₹ "+str(answer))

