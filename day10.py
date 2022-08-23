import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
 'what is your favorit clor?',
 ('blue','Red','Green'))

 st.write('Your favorite color is', option)
