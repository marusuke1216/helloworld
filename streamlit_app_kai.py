import streamlit as st

st.set_page_config(layout="wide")

st.title('How to layout your streamlit app')

with st.expander('About this app'):
 st.write('This app shows the various ways on how you can layout your Streamlit app.')
 st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Input')
st.sidebar.subheader('Input CSV')
uploaded_file = st.sidebar.file_uploader("Choose a file")

st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')
