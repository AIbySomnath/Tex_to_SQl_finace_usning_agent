import streamlit as st
from agent1 import main as agent1_main

st.title('Financial Data Analysis with AI Agents')

st.write("""
This application processes financial data using AI agents. 
You can request an account summary for the current month.
""")

command = st.text_input('Enter your command:', 'Give me the account summary for the current month')

if st.button('Run Command'):
    response = agent1_main(command)
    st.text(response)