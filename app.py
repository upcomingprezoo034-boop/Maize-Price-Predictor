import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Maize Price Forecast System",
    page_icon="🌽",
    layout="wide"
)

# Main title
st.title("🌽 Maize Price Forecast System")

st.write(
"""
Welcome to the **Maize Price Forecast System**.

This application helps farmers predict maize prices in **Nairobi and Kitui markets**.
"""
)

st.markdown("## How Farmers Can Use This System")

st.markdown("""
1️⃣ **Register as a farmer**

2️⃣ **Select your market**

3️⃣ **Choose prediction duration**

4️⃣ **View predicted maize prices**

5️⃣ **Explore price trends**
""")

st.info("Use the **sidebar** to navigate through the pages of the system.")

st.markdown("---")

st.subheader("Why This System Is Useful")

st.write(
"""
Farmers often sell their crops without knowing future market prices.

This system helps farmers:

- Predict maize prices
- Identify good markets
- Understand price trends
"""
)

st.success("Navigate using the sidebar on the left.")
