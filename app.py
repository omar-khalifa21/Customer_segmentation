import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
kmeans = joblib.load("customer_segmentor.pkl")
scaler = joblib.load("scaler.pkl")

# Set page config
st.set_page_config(page_title="Customer Segmentation App", page_icon="🧾", layout="centered")

# Dark mode styling
st.markdown(
    """
    <style>
        body {
            background-color: #0E1117;
            color: #FAFAFA;
        }
        .stButton>button {
            background-color: #FF4B4B;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            padding: 0.6em 1.2em;
        }
        .stNumberInput>div>div>input {
            background-color: #262730;
            color: #FAFAFA;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# App title
st.title("🧾 Customer Segmentation App")
st.write("Enter customer details below to predict their **customer segment**.")

# Input fields
col1, col2 = st.columns(2)

with col1:
    income = st.number_input("💰 Income", min_value=0, step=100, value=30000)
    total_spending = st.number_input("🛍️ Total Spending", min_value=0, step=100, value=5000)
    num_web_purchases = st.number_input("🌐 Number of Web Purchases", min_value=0, step=1, value=5)
    num_store_purchases = st.number_input("🏬 Number of Store Purchases", min_value=0, step=1, value=3)

with col2:
    num_web_visits = st.number_input("📅 Web Visits per Month", min_value=0, step=1, value=4)
    recency = st.number_input("⏳ Recency (days since last purchase)", min_value=0, step=1, value=20)
    age = st.number_input("🎂 Age", min_value=18, step=1, value=30)

# Prepare input dataframe
input_data = pd.DataFrame({
    "Income": [income],
    "total_spending": [total_spending],
    "NumWebPurchases": [num_web_purchases],
    "NumStorePurchases": [num_store_purchases],
    "NumWebVisitsMonth": [num_web_visits],
    "Recency": [recency],
    "Age": [age],
})

scaled_data = scaler.transform(input_data)

# Cluster labels for 6 clusters
cluster_labels = {
    0: "💎 High Income – High Spending",
    1: "🛒 Low Income – Budget Spenders",
    2: "⚡ Young – Online Shoppers",
    3: "🏪 Older – Store Shoppers",
    4: "📊 Moderate Income – Mixed Spending",
    5: "⏰ High Recency – Inactive Customers",
}

# Predict button
if st.button("🔍 Predict Segment"):
    segment = kmeans.predict(scaled_data)[0]
    segment_name = cluster_labels.get(segment, f"Cluster {segment}")

    st.success(f"✅ Predicted Customer Segment: **{segment_name}**")
    st.markdown("---")

    # Show details
    st.subheader("📌 Input Summary")
    st.write(input_data)
