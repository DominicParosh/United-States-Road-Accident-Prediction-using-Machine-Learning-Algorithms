import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
# from classify_page import classify_page

# streamlit run app.py 
page = st.sidebar.selectbox("Predict or Explore", ( "Predict","Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()

