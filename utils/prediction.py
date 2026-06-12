def diabetes_prediction(glucose, bp, bmi, age):

    score = 0

    if glucose > 140:
        score += 40

    if bp > 130:
        score += 20

    if bmi > 30:
        score += 20

    if age > 45:
        score += 20

    if score >= 60:
        return "High Risk"

    elif score >= 30:
        return "Medium Risk"

    else:
        return "Low Risk"


def heart_prediction(age, cholesterol, bp):

    score = 0

    if age > 50:
        score += 30

    if cholesterol > 240:
        score += 40

    if bp > 140:
        score += 30

    if score >= 60:
        return "High Risk"

    elif score >= 30:
        return "Medium Risk"

    else:
        return "Low Risk"