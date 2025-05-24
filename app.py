# page1_predict_disease.py
import streamlit as st
import requests
import pandas as pd

# Define your symptoms list (you can expand this)
SYMPTOMS_LIST = ["Fever", "Cough", "Fatigue", "Headache", "Nausea", "Sore Throat", "Runny Nose"]

st.title("🧠 Disease Prediction")

# 1. Age Input
age = st.number_input("Enter your age", min_value=0, max_value=120, step=1)

# 2. Gender Selection
gender = st.selectbox("Select your gender", ["Male", "Female"])

# 3. Symptom Selection using Checkboxes
st.subheader("Select the symptoms you have:")
selected_symptoms = []
symptom_flags = {}

# Dynamically show checkboxes
for symptom in SYMPTOMS_LIST:
    checked = st.checkbox(symptom)
    selected_symptoms.append(symptom if checked else None)
    symptom_flags[symptom] = 1 if checked else 0

# 4. Submit Button
if st.button("Predict Disease"):
    # Create payload for API or model
    input_data = {
        "age": age,
        "gender": gender.lower(),  # lowercase for consistency
        **{symptom.lower().replace(" ", "_"): flag for symptom, flag in symptom_flags.items()}
    }

    try:
        # Replace the URL with your actual ML model API endpoint
        # response = requests.post("http://localhost:8000/predict", json=input_data)
        # prediction = response.json().get("prediction", "Unknown")

        # Temporary placeholder logic
        prediction = "Flu" if input_data.get("fever", 0) and input_data.get("cough", 0) else "Common Cold"

        st.success(f"✅ Predicted Disease: **{prediction}**")

    except Exception as e:
        st.error("❌ Error occurred during prediction.")
        st.exception(e)
