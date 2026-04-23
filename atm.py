#-----Streamlit Python Framework-----#
# In this .py file, I started working on Streamlit python framework.

import streamlit as st

st.set_page_config(page_title='Welcome to ATM', layout='centered')

if 'Balance' not in st.session_state:
    st.session_state.balance = 1000

st.title('Welcome to the Automated Tailer Machine')
st.markdown('___')
st.header(f'Current Balance: LKR {st.session_state.balance:.2f}')

st.subheader('Deposits')
deposit_amount = st.number_input('Enter amount to deposit: ', min_value=0.01, format='%.2f', key='deposit_input')
if st.button('Deposit', key='deposit_button'):
    if deposit_amount > 0:
        st.session_state.balance += deposit_amount
        st.success(f'Successfully Deposited LKR{deposit_amount}:.2f.')
        st.experimental_rerun()
    else:
        st.error('Invalid Deposit Amount!!!')
st.markdown('___')

st.subheader('Withdrawals')
withdrawal_amount = st.number_input('Enter amount to withdraw: ', min_value=0.01, format='%.2f', key='withdraw_input')
if st.button('Withdraw', key='withdraw_button'):
    if withdrawal_amount > 0:
        if st.session_state.balance >= withdrawal_amount:
            st.session_state.balance -= withdrawal_amount
            st.success(f"Successfully withdrew ${withdrawal_amount:.2f}.")
            st.experimental_rerun() # Rerun to update balance display
        else:
            st.error("Insufficient funds.")
    else:
        st.error("Withdrawal amount must be greater than zero.")

st.markdown("--- ")
st.info("Thank you for using the Simple ATM!")