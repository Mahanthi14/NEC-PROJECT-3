def recommend_treatment(disease):

    recommendations = {

        "Diabetes":
        "Endocrinologist consultation, HbA1c test, diet control",

        "Heart Disease":
        "Cardiologist consultation, ECG, Lipid Profile",

        "Kidney Disease":
        "Nephrologist consultation, Creatinine Test",

        "Cancer Risk":
        "Oncologist consultation, MRI/CT Scan"
    }

    return recommendations.get(
        disease,
        "General Physician Consultation"
    )