import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Maize Market Trends")

st.write("Historical maize price trends")

data = pd.read_excel("maize_dataset.xlsx")

st.write(data.head())

fig, ax = plt.subplots()

ax.plot(data["Year"], data["Price"])

ax.set_xlabel("Year")
ax.set_ylabel("Price (KSh)")

st.pyplot(fig)
