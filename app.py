import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("food_waste_model.pkl", "rb"))

st.title("🌾 AI-Powered Food Waste Prediction & Redistribution System")

st.markdown(
"""
This AI system predicts food waste generation and provides
redistribution recommendations.
"""
)

center = st.number_input("Center ID", min_value=0)
meal = st.number_input("Meal ID", min_value=0)
people = st.number_input("Expected Number of People", min_value=0)
quantity = st.number_input("Food Prepared (kg)", min_value=0)


if st.button("🔮 Predict Waste"):

    input_data = np.array([
        [center, meal, people, quantity]
    ])

    prediction = model.predict(input_data)

    waste = round(float(prediction[0]),2)

    st.success(
        f"📊 Predicted Food Waste: {waste} kg"
    )


    if waste > 50:
        st.warning(
            "⚠️ High Waste Detected"
        )
        st.info(
            "🤝 Suggested NGOs: Feeding India, Red Cross"
        )
        st.info(
            "⚡ Redistribute within 4–6 hours"
        )

    else:
        st.success(
            "✅ Waste level is manageable"
        )
