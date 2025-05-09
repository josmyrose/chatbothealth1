
import streamlit as st
from model import train_model, predict_disease
from chatbot import llm_response

st.set_page_config(page_title="Disease Prediction Chatbot")

st.title("🩺 Symptom-based Disease Predictor")

clf, symptoms = train_model()

user_input = st.text_input("Describe your symptoms (comma-separated):")

if user_input:
    st.markdown("### 🤖 Chatbot Says:")
    llm_reply = llm_response(user_input)
    st.write(llm_reply)

    input_symptoms = user_input.lower().split(',')
    input_vector = {symptom: 1 if symptom.strip() in input_symptoms else 0 for symptom in symptoms}

    predicted_disease = predict_disease(input_vector)
    st.success(f"🔍 Based on your symptoms, you may have: **{predicted_disease}**")
