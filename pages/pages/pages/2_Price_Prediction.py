import streamlit as st
import pandas as pd
import pickle

st.title("Maize Price Prediction")

# Load dataset
data = pd.read_excel("maize_dataset.xlsx")

# Load trained model
model = pickle.load(open("price_prediction_model.pkl", "rb"))

st.write("Select market and prediction duration")

# Get markets from dataset automatically
markets = sorted(data["Market"].unique())

market = st.selectbox("Select Market", markets)

# Prediction duration
duration = st.selectbox(
"Prediction Period",
[
"Next Week",
"Next Month",
"3 Months",
"6 Months"
]
)

# Convert duration into numeric value
duration_map = {
"Next Week":1,
"Next Month":4,
"3 Months":12,
"6 Months":24
}

duration_value = duration_map[duration]

if st.button("Predict Price"):

    # Create input dataframe for model
    input_data = pd.DataFrame({
        "Market":[market],
        "Duration":[duration_value]
    })

    # Convert market to numeric if needed
    input_data = pd.get_dummies(input_data)

    prediction = model.predict(input_data)

    predicted_price = round(prediction[0],2)

    st.success(
        f"Estimated maize price in {market} after {duration} is KSh {predicted_price} per bag."
    )
