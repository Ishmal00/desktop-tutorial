import streamlit as st
import pandas as pd
from model_predictor import ModelPredictor

# Set up Streamlit UI
st.set_page_config(page_title="California House Price Predictor", layout="centered")

st.markdown("## 🏡 California House Price Prediction App")
st.markdown("Enter house details below to get an estimated price:")

# Input fields (dummy fields matching trained model)
longitude = st.slider("🌐 Longitude", min_value=-125.0, max_value=-113.0, step=0.01, value=-120.0)
latitude = st.slider("📍 Latitude", min_value=32.0, max_value=42.0, step=0.01, value=36.0)
beds = st.number_input("🛏 Bedrooms", min_value=1, max_value=10, value=3)
baths = st.number_input("🛁 Bathrooms", min_value=1, max_value=10, value=2)
size = st.number_input("📐 Size (sqft)", min_value=100, max_value=10000, value=1500)
lot_size = st.number_input("🌳 Lot Size (sqft)", min_value=100, max_value=20000, value=3000)
zip_code = st.text_input("📍 ZIP Code", value="90210")


# Create DataFrame (must match model features)
input_data = pd.DataFrame({
    'beds': [beds],
    'baths': [baths],
    'size': [size],
    'lot_size': [lot_size],
    'zip_code': [zip_code]
})

# Load model and predict
try:
    predictor = ModelPredictor(model_path='svm_classifier.pkl', scaler_path='scaler.pkl')
    if st.button("🔍 Predict Price"):
        prediction = predictor.predict(input_data)
        st.success(f"💰 Estimated House Price: **${prediction[0]:,.0f}**")
except Exception as e:
    st.error(f" Error: {str(e)}")

st.markdown("---")
st.caption("Developed as part of OOP Phase 2 — by Ishmal Nadeem")




