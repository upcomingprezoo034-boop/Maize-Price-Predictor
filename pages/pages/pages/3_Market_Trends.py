import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Market Trends and Seasonal Data")

data = pd.read_excel("maize_dataset.xlsx")

st.write("Historical maize prices")

fig, ax = plt.subplots()

ax.plot(data["Year"], data["Price"])

ax.set_xlabel("Year")
ax.set_ylabel("Price (KSh)")

st.pyplot(fig)

st.write("Higher prices normally occur during dry seasons.")
