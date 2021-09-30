# imports
import streamlit as st
import pickle
import numpy as np

# header
st.title('OurAPP')

# user inputs
case_type = st.text_input("Enter Case Type:* (ex. 1,2,3)")
age = st.text_input("Enter Offender Age:* ")

# set up X columns
# X = []
