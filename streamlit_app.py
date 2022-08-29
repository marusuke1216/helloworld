import streamlit as st
from datetime import time, datetime

st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
 [theme]
 primaryColor="zzzzzzz"
 backgroundColor="#2E86C1"
 secondaryBackgroundColor="#AED6F1"
 textColor="#FFFFFF"
 font="monospace"
 """)

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)


appointment = st.slider(
  "Schedule your appointment:",
  value=(time(11, 30), time(12, 45)))
st.write("you're scheduled for:",appointment)

st.subheader('datetime slider')

start_time = st.slider(
  "When do you start?",
  value=datetime(2020,1,1,9,30),
  format="MM/DD/YY - hh:mm")
st.write("start timee:",start_time)

start_time = st.slider(
  "When do you start?",
  value=datetime(2020,1,1,9,30),
  format="MM/DD/YY - hh:mm")
st.write("git追加:",start_time)
