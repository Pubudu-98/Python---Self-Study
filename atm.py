#-----Streamlit Python Freamework-----#
# In this .py file, I started working on Streamlit python freamework.

import streamlit as st

st.set_page_config(page_title='Welcome to ATM', layout='centered')

if 'Balance' not in st.session_state:
    st.session_state.balance = 1000

st.title('Welcome to the ATM')
st.markdown('___')
st.header(f'Current Balance: LKR {st.session_state.balance:.2f}')