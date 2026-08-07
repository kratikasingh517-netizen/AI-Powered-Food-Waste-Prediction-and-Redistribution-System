import streamlit as st

st.title("🌾 Food Waste AI System")

center = st.text_input("Enter Center ID")
meal = st.text_input("Enter Meal ID")

if st.button("Predict"):
    st.write("📊 Predicted Waste: 120 kg")
    st.write("🤝 NGO Suggestions: Feeding India, Red Cross")
    st.write("⚡ Recommendation: Distribute within 4–6 hours")
