!pip install joblib

import streamlit as st
import joblib

st.set_page_config(page_title="Disease Predictor", layout="centered")
st.title("🩺 Disease Prediction from Symptoms")

# Load the model
# @st.cache_resource
# def load_model():
#     return joblib.load("disease_model.pkl")

# model = load_model()

SYMPTOMS_LIST = [
    "Fever", "Cough", "Fatigue", "Headache", "Nausea",
    "Sore Throat", "Runny Nose", "Muscle Pain", "Diarrhea", "Vomiting"
]

# User inputs
age = st.number_input("Enter your age:", min_value=1, max_value=120, step=1)
gender = st.selectbox("Select your gender:", ["Male", "Female"])
selected_symptoms = st.multiselect("Select your symptoms:", SYMPTOMS_LIST)

# Submit
if st.button("Predict Disease"):
    symptom_vector = [1 if symptom in selected_symptoms else 0 for symptom in SYMPTOMS_LIST]
    gender_numeric = 1 if gender == "Male" else 0
    input_vector = [age, gender_numeric] + symptom_vector

    try:
        prediction = model.predict([input_vector])[0]
        st.success(f"✅ Predicted Disease: **{prediction}**")
    except Exception as e:
        st.error("Prediction failed.")
        st.exception(e)
