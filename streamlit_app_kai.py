import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title('How to layout your streamlit app')

with st.expander('About this app'):
 st.write('This app shows the various ways on how you can layout your Streamlit app.')
 st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Input')
st.sidebar.subheader('Input CSV')
uploaded_file = st.sidebar.file_uploader("Choose a file")


st.header('Output')

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.plot)
  st.write(df.describe())
  st.sidebar.balloons()
else:
  st.info('☝️ Upload a CSV file')
