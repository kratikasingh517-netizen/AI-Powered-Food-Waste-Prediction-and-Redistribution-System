import streamlit as st

st.title("🌾 Food Waste AI System")

center = st.text_input("Enter Center ID")
meal = st.text_input("Enter Meal ID")

if st.button("Predict"):
    st.write("📊 Predicted Waste: 120 kg")
    st.write("🤝 NGO Suggestions: Feeding India, Red Cross")
    st.write("⚡ Recommendation: Distribute within 4–6 hours")
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
