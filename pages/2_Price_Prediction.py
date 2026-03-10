import streamlit as st
import pandas as pd
import pickle

st.title("Maize Wholesale Price Prediction")

st.write("Enter seasonal conditions to estimate maize prices.")

# Load trained model
model = pickle.load(open("Untitled2.ipynb","rb"))

# Farmer inputs
rainfall = st.number_input(
"Expected Rainfall (mm)",
min_value=0.0,
max_value=500.0,
value=100.0
)

season = st.selectbox(
"Season",
[
"Planting",
"Growing",
"Harvest",
]
)

# Convert season to numeric
season_map = {
"Planting":1,
"Growing":2,
"Harvest":3,
}

season_value = season_map[season]

if st.button("Predict Wholesale Price"):

    input_data = pd.DataFrame({
        "Rainfall":[rainfall],
        "Season":[season_value]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Predicted wholesale maize price is KSh {round(prediction[0],2)} per bag."
    )
