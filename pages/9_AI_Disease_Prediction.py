import streamlit as st
import joblib
import numpy as np
from pathlib import Path

st.set_page_config(page_title="AI Disease Prediction", page_icon="🤖", layout="wide")

st.title("🤖 AI Disease Prediction Module")
st.write("ML-based disease prediction using trained Random Forest models.")

DIABETES_MODEL_PATH = "models/diabetes_model.pkl"
HEART_MODEL_PATH = "models/heart_model.pkl"

def predict_diabetes(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age):
    if not Path(DIABETES_MODEL_PATH).exists():
        return "Diabetes model not found", 0

    model = joblib.load(DIABETES_MODEL_PATH)
    data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])
    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1] * 100

    if prediction == 1:
        return "Diabetes Risk Detected", round(probability, 2)
    return "Low Diabetes Risk", round(probability, 2)

def predict_heart(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    if not Path(HEART_MODEL_PATH).exists():
        return "Heart model not found", 0

    model = joblib.load(HEART_MODEL_PATH)
    data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1] * 100

    if prediction == 1:
        return "Heart Disease Risk Detected", round(probability, 2)
    return "Low Heart Disease Risk", round(probability, 2)

tab1, tab2 = st.tabs(["🩸 Diabetes Prediction", "❤️ Heart Disease Prediction"])

with tab1:
    st.subheader("Diabetes Risk Prediction")

    col1, col2 = st.columns(2)

    with col1:
        pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=2)
        glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=120)
        blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=200, value=80)
        skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=25)

    with col2:
        insulin = st.number_input("Insulin Level", min_value=0, max_value=900, value=80)
        bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
        diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
        age = st.number_input("Age", min_value=1, max_value=120, value=30)

    if st.button("Predict Diabetes Risk", use_container_width=True):
        result, probability = predict_diabetes(
            pregnancies, glucose, blood_pressure, skin_thickness,
            insulin, bmi, diabetes_pedigree, age
        )

        st.metric("Prediction Result", result)
        st.metric("Risk Probability", f"{probability}%")

        if "Detected" in result:
            st.error("Severity Level: High")
            st.warning("Recommendation: Consult an endocrinologist and check HbA1c.")
        else:
            st.success("Severity Level: Low")
            st.info("Recommendation: Maintain a healthy lifestyle and regular checkups.")

with tab2:
    st.subheader("Heart Disease Risk Prediction")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Patient Age", min_value=1, max_value=120, value=45)
        sex = st.selectbox("Sex", ["Female", "Male"])
        cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
        trestbps = st.number_input("Resting Blood Pressure", min_value=0, max_value=250, value=120)
        chol = st.number_input("Cholesterol Level", min_value=0, max_value=600, value=200)
        fbs = st.selectbox("Fasting Blood Sugar > 120", [0, 1])

    with col2:
        restecg = st.selectbox("Resting ECG", [0, 1, 2])
        thalach = st.number_input("Maximum Heart Rate", min_value=0, max_value=250, value=150)
        exang = st.selectbox("Exercise Induced Angina", [0, 1])
        oldpeak = st.number_input("Oldpeak", min_value=0.0, max_value=10.0, value=1.0)
        slope = st.selectbox("Slope", [0, 1, 2])
        ca = st.selectbox("Number of Major Vessels", [0, 1, 2, 3])
        thal = st.selectbox("Thal", [1, 2, 3])

    if st.button("Predict Heart Disease Risk", use_container_width=True):
        sex_value = 1 if sex == "Male" else 0

        result, probability = predict_heart(
            age, sex_value, cp, trestbps, chol, fbs,
            restecg, thalach, exang, oldpeak, slope, ca, thal
        )

        st.metric("Prediction Result", result)
        st.metric("Risk Probability", f"{probability}%")

        if "Detected" in result:
            st.error("Severity Level: High")
            st.warning("Recommendation: Consult a cardiologist and take ECG/Lipid Profile.")
        else:
            st.success("Severity Level: Low")
            st.info("Recommendation: Maintain a healthy diet and monitor BP.")