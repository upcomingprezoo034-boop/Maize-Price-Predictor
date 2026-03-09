import streamlit as st
import pickle
import pandas as pd

st.title("Maize Price Prediction")

markets = [
"Nairobi-Kangemi",
"Nairobi-Wakulima",
"Nairobi-Gikomba",
"Nairobi-Kawangware",
"Nairobi-Kariobangi",
"Kitui-Town",
"Kitui-Mwingi",
"Kitui-Mutomo",
"Kitui-Kitui Market"
]

market = st.selectbox("Select Market", markets)

timeline = st.selectbox(
"Prediction Period",
[
"Next Week",
"Next Month",
"3 Months",
"6 Months"
]
)

if st.button("Predict Price"):

    # Example predicted values
    predicted_price = 3200

    st.success(
        f"Estimated maize price at {market} during {timeline} is about KSh {predicted_price} per bag."
    )
