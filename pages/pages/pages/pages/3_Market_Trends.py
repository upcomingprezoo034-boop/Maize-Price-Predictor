import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Maize Market Trends")

data = pd.read_excel("maize_dataset.xlsx")

markets = sorted(data["Market"].unique())

market = st.selectbox("Select Market", markets)

market_data = data[data["Market"] == market]

st.write("Historical price data")

st.dataframe(market_data)

fig, ax = plt.subplots()

ax.plot(market_data["Year"], market_data["Price"])

ax.set_xlabel("Year")
ax.set_ylabel("Price (KSh)")
ax.set_title(f"{market} Price Trend")

st.pyplot(fig)
