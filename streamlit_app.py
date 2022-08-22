import streamlit as st
from datetime import time, datetime

st.header('st.slider')

st.subheader('slider')

age = st.slider('How old are you',0,130,25)
st.write("I'm",age,'years old')

st.subheader('Range slider')

values = st.slider(
   'Salect a range of values',
   0.0,100.0,(25.0,75.0))
st.write('values:',values)

st.subheader('Range time slider')

appointment = st.slider(
  "Schedule your appointment:",
  value=(time(11, 30), time(12, 45)))
st.write("you're scheduled for:",apppintoment)

st.subheader('datetime slider')

start_time = st.slider(
  "When do you start?",
  value=datetime(2020,1,1,9,30),
  format="MM/DD/YY - hh:mm")
st.write("start timee:",start_time)
