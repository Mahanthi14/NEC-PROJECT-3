def analyze_report(
        hemoglobin,
        sugar,
        cholesterol):

    alerts = []

    if hemoglobin < 10:
        alerts.append(
            "Low Hemoglobin"
        )

    if sugar > 180:
        alerts.append(
            "High Blood Sugar"
        )

    if cholesterol > 240:
        alerts.append(
            "High Cholesterol"
        )

    return alerts