import streamlit as st
import pickle
import numpy as np

# Load ML model
model = pickle.load(open("food_waste_model.pkl", "rb"))

st.title("🌾 AI-Powered Food Waste Prediction & Redistribution System")

st.write(
    "Predict food waste generation and get redistribution recommendations using AI."
)

center = st.number_input("Enter Center ID")
meal = st.number_input("Enter Meal ID")
people = st.number_input("Expected Number of People")
quantity = st.number_input("Food Quantity Prepared (kg)")

if st.button("Predict Waste"):

    input_data = np.array([[center, meal, people, quantity]])

    prediction = model.predict(input_data)

    waste = round(prediction[0], 2)

    st.success(f"📊 Predicted Food Waste: {waste} kg")

    if waste > 50:
        st.info("🤝 NGO Suggestions: Feeding India, Red Cross")
        st.warning("⚡ Recommendation: Redistribute within 4–6 hours")
    else:
        st.success("✅ Waste level is manageable")
