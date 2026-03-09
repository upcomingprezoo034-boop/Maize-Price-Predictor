import streamlit as st

st.title("Farmer Registration")

st.write("Please register before predicting maize prices.")

name = st.text_input("Farmer Name")
crop = st.selectbox(
    "Crop Produced",
    ["Maize", "Beans", "Green Grams", "Sorghum"]
)

password = st.text_input("Create Password", type="password")

if st.button("Register"):
    if name == "":
        st.warning("Please enter your name")
    else:
        st.success(f"Welcome {name}! Registration successful.")
