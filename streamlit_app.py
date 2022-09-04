import streamlit as st

st.title('st.session_state')

def lbs_to_kg():
    st.session_state.kgs = st.session_state.lbss/2.2046
def kg_to_lbs():
    st.session_state.lbsd = st.session_state.kgs*2.2046

st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
    pounds = st.number_input("Pounds:", key = "lbss", on_change = lbs_to_kg)
with col2:
    kloglaram = st.number_input("kilograms:", key = "kgs", on_change = kg_to_lbs)

st.header('Output')
st.write("st.session_state object:", st.session_state)
