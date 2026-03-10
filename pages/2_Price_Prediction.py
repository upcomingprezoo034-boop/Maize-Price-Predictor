import streamlit as st
import pandas as pd
import pickle

st.title("Maize Price Predictor")

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

st.write("Select your market and prediction period")

# Real markets from dataset
markets = sorted(data["Market"].dropna().unique())

market = st.selectbox("Choose Market", markets)

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
