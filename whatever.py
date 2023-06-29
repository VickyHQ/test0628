import pandas as pd
import streamlit as st

header= st.container()
dataset = st.container()
features= st.container()
modelTraining= st.container()

with header:
    st.title('Welcome to my awesome data science project!')
    st.text('transactions of taxis in NYC')

with dataset:
    st.header('NYC taxi dataset')

with features:
    st.header('The features I created')

with modelTraining:
    st.header('Time to train the model')
    