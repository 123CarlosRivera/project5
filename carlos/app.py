# imports
import streamlit as st
import pickle
import numpy as np

# header
st.title('OurAPP')

# user inputs
disposit = st.text_input("Enter diposition of defendants case:* (ex. 0-5)")
drugmin = st.text_input("Offense mandatory minimum?:* (In Months) ")
mweight = st.text_input("Amount of Marijuana in grams:* (Grams)")
numdepen = st.text_input("Number of family dependants:* (ex. 1,2,3)")
statmax = st.text_input("Max months in prison for offense:* (ex. 1,2,3)")
statmin = st.text_input("Minimum amount of months in prison for offense:* (ex. 1,2,3)")
sources = st.text_input("Strength of evidence:* ex(1-3 or 5-9)")



# Default features
accgdln = 1 # Court does accept explicit statements
district = 1 # Massachusetts
intdum = 0 # did the offender recieve intermitten confinement
methmin = 0 # mandatory minimum sentence for meth manufactoring
nodrug = 1 # number of different drugs involved
offguide = 9 # offense guidline, 9 is for drug possession
quarter = 4 # July 1 thru Sept 30
casetype = 2 # Misdemeanor A
crimhist = 0 # no criminal History
combdrg2 = 4 # we're only working with marijuana cases
dsplea = 3
reas1 = 1
reas2 = 2
reas3 = 3
# set X features for modeling
X = [[
            accgdln, casetype, combdrg2,
            crimhist, int(disposit), district,
            int(drugmin), dsplea, intdum,
            methmin, int(mweight),nodrug,
            offguide,quarter, reas1,
            reas2, reas3, int(numdepen),
            int(sources), int(statmax), int(statmin)
]]

#st.write(X)

# when it comes to defaults, if probatn is greater than 0, probdum is 1 (yes, defendant recieved probabtion)
# load in models for voting
with open('../carlos/app_models/logreg.pkl', 'rb') as pickle_in:
    logreg = pickle.load(pickle_in)
# condition to make sure that each input is recieved
prediction = logreg.predict(X)

if prediction==1:
    st.write(f"The verdict most likely is {prediction}")
