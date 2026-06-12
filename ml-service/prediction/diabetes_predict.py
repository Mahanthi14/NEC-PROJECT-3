import joblib
import numpy as np
from pathlib import Path

MODEL_PATH = "models/diabetes_model.pkl"

def predict_diabetes(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age):
    if not Path(MODEL_PATH).exists():
        return "Model not trained", 0

    model = joblib.load(MODEL_PATH)

    data = np.array([[
        pregnancies, glucose, blood_pressure, skin_thickness,
        insulin, bmi, diabetes_pedigree, age
    ]])

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1] * 100

    if prediction == 1:
        return "Diabetes Risk Detected", round(probability, 2)
    else:
        return "Low Diabetes Risk", round(probability, 2)