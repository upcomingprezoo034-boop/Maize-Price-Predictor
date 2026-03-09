import streamlit as st
import pandas as pd
import numpy as np

st.title("Maize Price Prediction")

st.write("Enter the values below to predict maize price")

rainfall = st.number_input("Rainfall (mm)")
supply = st.number_input("Supply volume")
season = st.selectbox("Season", ["Planting", "Growing", "Harvest"])

if st.button("Predict Price"):
    
    # Example simple formula (we will replace with your real model later)
    price = 20 + (0.02 * rainfall) - (0.01 * supply)
    
    st.success(f"Predicted maize price: {price:.2f} KSh/kg")
