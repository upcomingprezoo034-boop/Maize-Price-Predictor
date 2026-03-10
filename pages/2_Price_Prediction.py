import streamlit as st
import pandas as pd
import numpy as np

st.title("Maize Price Prediction App")

# Load dataset safely
@st.cache_data
def load_data():
    return pd.read_excel("maize_dataset.xlsx")

data = load_data()

# Load trained model safely
@st.cache_resource
def load_model():
    with open("price_prediction_model.pkl","rb") as f:
        return pickle.load(f)

model = load_model()

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
        "Nairobi-Nyamakima": 54,
        "Nairobi-Kawangware": 56,
        "Naiobi-Nairobi wakulima": 58,
        "Kitui-Mwingi town": 53,
        "Kitui-Kisasi": 52,
        "Kitui-Tseikuru": 51,
        "Kitui-Kalundu Market": 52,
        "Kitui-Kabati Market": 50
    }

    price = base_prices[market]

    
timeline = st.selectbox(
"Prediction Duration",
[
"1 Week",
"1 Month",
"3 Months"
]
)

# Convert duration to number
timeline_map = {
"1 Week":1,
"1 Month":4,
"3 Months":12
}

duration_value = timeline_map[timeline]

if st.button("Predict Price"):

    try:

        # Example input structure
        input_df = pd.DataFrame({
            "Market":[market],
            "Duration":[duration_value]
        })

        # Convert categorical variables
        input_df = pd.get_dummies(input_df)

        prediction = model.predict(input_df)

        st.success(
            f"Predicted maize price in {market} after {timeline} is KSh {round(prediction[0],2)} per bag."
        )

    except Exception as e:
        st.error("Prediction failed. Model input format may not match training data.")
        st.write(e)
