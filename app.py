import streamlit as st
from model import predict_price

st.set_page_config(page_title="House Price Prediction")

st.title("🏠 House Price Prediction")
st.write("Machine Learning Model using Linear Regression")

area = st.number_input("Enter Area (sq ft)", min_value=500, max_value=5000)
bedrooms = st.number_input("Enter Number of Bedrooms", min_value=1, max_value=10)
age = st.number_input("Enter House Age (years)", min_value=0, max_value=50)

if st.button("Predict Price"):
    price = predict_price(area, bedrooms, age)
    st.success(f"Estimated House Price: ₹ {int(price):,}")

