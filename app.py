import streamlit as st
from predict import show_prediction
from explore import show_explore

pages = st.sidebar.selectbox("Explore or Predict", ("Predict", "Explore"))

if pages == "Predict":
    show_prediction()
else:
    show_explore()
