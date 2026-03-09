import streamlit as st

st.title("Maize Price Predictor")

st.write("Choose your market and prediction duration")

# Market options
markets = [
"Nairobi - Wakulima",
"Nairobi - Gikomba",
"Nairobi - Kangemi",
"Nairobi - Kawangware",
"Kitui - Town Market",
"Kitui - Mwingi Market",
"Kitui - Mutomo Market"
]

market = st.selectbox("Select Market", markets)

# Prediction time
duration = st.selectbox(
"Prediction Duration",
[
"Next Week",
"Next Month",
"3 Months",
"6 Months"
]
)

if st.button("Predict Price"):

    predicted_price = 3200

    st.success(
        f"Estimated maize price in {market} during {duration} is about KSh {predicted_price} per bag."
    )
