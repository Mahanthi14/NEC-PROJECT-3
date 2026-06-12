import joblib
import numpy as np
from pathlib import Path

MODEL_PATH = "models/heart_model.pkl"

def predict_heart(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    if not Path(MODEL_PATH).exists():
        return "Model not trained", 0

    model = joblib.load(MODEL_PATH)

    data = np.array([[
        age, sex, cp, trestbps, chol, fbs,
        restecg, thalach, exang, oldpeak, slope, ca, thal
    ]])

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1] * 100

    if prediction == 1:
        return "Heart Disease Risk Detected", round(probability, 2)
    else:
        return "Low Heart Disease Risk", round(probability, 2)