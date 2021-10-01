# imports
import streamlit as st
import pickle
import numpy as np
from PIL import Image
from sklearn.preprocessing import StandardScaler
# Header image
col1, col2, col3 = st.beta_columns(3)
image1 = Image.open('/Users/crivera/Desktop/project5/assets/US_SentencingCom_Symbol.JPG')
col1.image(image1,use_column_width=True)
image2 = Image.open('/Users/crivera/Desktop/project5/assets/US_SentencingCom_Symbol.JPG')
col2.image(image2,use_column_width=True)
image3 = Image.open('/Users/crivera/Desktop/project5/assets/US_SentencingCom_Symbol.JPG')
col3.image(image3,use_column_width=True)
st.title('=Judge Analyzer By GA Data Engineers=')

# Sidebar setup
page = st.sidebar.selectbox('Select a category:',
('About','Predict'))

if page=='About':
    st.write("This app was designed for use by anyone representing a person convicted of a criminal offense. Please enter the relevant information into the fields on the site; the app will then predict whether the defendant will receive prison time. This predictive tool can be used to assess the likelihood that a case was misclassified or mishandled, thereby helping lawyers focus on appealing those cases that fall into these categories.")
    st.write("Behind the scenes, this application predicts whether a defendant will receive a prison sentence or alternative sentence using a variety of models trained on data from the United States Sentencing Commission taken in the fiscal year 2020. Each model gets one “vote” in determining the final prediction.")
if page=='Predict':

    # user inputs
    disposit = st.text_input("Enter diposition of defendants case:* (ex. 0-5)")
    mweight = st.text_input("Amount of Marijuana in grams:* (ex. Grams)")
    numdepen = st.text_input("Number of family dependants:* (ex. 1,2,3)")
    statmax = st.text_input("Max months in prison for offense:* (ex. 1,2,3)")
    #statmin = st.text_input("Minimum amount of months in prison for offense:* (ex. 1,2,3)")
    sources = st.text_input("Strength of evidence:* (ex. 1-3 or 5-9)")



    # Default features
    accgdln = 1 # Court does accept explicit statements
    district = 1 # Massachusetts
    intdum = 0 # did the offender recieve intermitten confinement
    methmin = 0 # mandatory minimum sentence for meth manufactoring
    nodrug = 1 # number of different drugs involved
    offguide = 9 # offense guidline, 9 is for drug possession
    quarter = 4 # July 1 thru Sept 30
    casetype = 2 # Misdemeanor A
    crimhist = 0 # No criminal History
    combdrg2 = 4 # we're only working with marijuana cases
    dsplea = 3
    reas1 = 1
    reas2 = 2
    reas3 = 3

    # load in models for voting
    with open('../carlos/app_models/knn.pkl', 'rb') as pickle_in:
            knn = pickle.load(pickle_in)
    with open('../carlos/app_models/dt.pkl', 'rb') as pickle_in:
            dt = pickle.load(pickle_in)
    with open('../carlos/app_models/et.pkl', 'rb') as pickle_in:
            et = pickle.load(pickle_in)
    with open('../carlos/app_models/rf.pkl', 'rb') as pickle_in:
            rf = pickle.load(pickle_in)
    with open('../carlos/app_models/bag.pkl', 'rb') as pickle_in:
            bag = pickle.load(pickle_in)

    # condition to make sure all required input is received
    if disposit == "" or mweight == "" or numdepen == "" or sources == "" or statmax== "": #or statmin== "":
        st.write("*Please answer all questions!!*")

    else:
        # set X features for modeling
        X = [[
                        accgdln, casetype, combdrg2,
                        crimhist, int(disposit), district,
                        dsplea, intdum,
                        methmin, int(mweight),nodrug,
                        offguide,quarter, reas1,
                        reas2, reas3, int(numdepen),
                        int(sources), int(statmax), #int(statmin)
        ]]

        # Do we need to Scale the inputs?
        # Do we need to Scale the inputs?
        # Do we need to Scale the inputs?
        # Do we need to Scale the inputs?
        # Do we need to Scale the inputs?
        # Do we need to Scale the inputs?
        # Do we need to Scale the inputs?
        # Do we need to Scale the inputs?



        ss = StandardScaler()
        X_ss = ss.fit_transform(X)

        knn_vote = knn.predict(X_ss)
        dt_vote = dt.predict(X_ss)
        et_vote = et.predict(X_ss)
        rf_vote = rf.predict(X_ss)
        bag_vote = bag.predict(X_ss)

        model_votes = [knn_vote,dt_vote,et_vote,rf_vote,bag_vote]
        vote_1 = 0
        for vote in model_votes:
            if vote == 1:
                vote_1+=1
            else:
                pass

        # if the vote count is 3 or greater, than the classification is prison time
        if vote_1>=3:
            st.write(f"{dt.predict_proba(X)[0][1]*100}% chance of receiving a prison sentence after conviction.")
        else:
            st.write(f"{dt.predict_proba(X)[0][0]*100}% chance of receiving a non-prison sentence after conviction!")
