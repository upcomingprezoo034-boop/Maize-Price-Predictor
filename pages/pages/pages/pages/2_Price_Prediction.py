import streamlit as st
import pandas as pd
import numpy as np

st.title("Maize Price Prediction App")

st.write("Select the market and prediction period to estimate maize price.")

# MARKET SELECTION
market = st.selectbox(
    "Select Market",
    ["Nairobi-Kangemi Market",
     "Nairobi-Gikomba Market",
     "Kitui-Kalundu Market",
     "Kitui-Kabati Market"]
)

# TIME SELECTION
time_period = st.selectbox(
    "Prediction Time",
    ["Next Week", "Next Month"]
)

# BUTTON
if st.button("Predict Price"):

    # Example base prices (you can later replace with real model)
    base_prices = {
        "Nairobi-Kangemi Market": 58,
        "Nairobi-Gikomba Market": 55,
        "Kitui-Kalundu Market": 52,
        "Kitui-Kabati Market": 50
    }

    price = base_prices[market]

    # Simple adjustment depending on time period
    if time_period == "Next Week":
        predicted_price = price + 1
    else:
        predicted_price = price + 3

    st.subheader("Predicted Maize Price")

    st.success(
        f"The predicted maize price for {market} in {time_period} is **{predicted_price} KSh/kg**"
    )
