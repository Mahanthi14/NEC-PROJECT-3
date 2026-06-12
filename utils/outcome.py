def predict_outcome(severity):

    if severity == "Critical":
        return {
            "Recovery": "35%",
            "ICU": "Required",
            "Stay": "10-15 Days"
        }

    elif severity == "High":
        return {
            "Recovery": "60%",
            "ICU": "Possible",
            "Stay": "7-10 Days"
        }

    elif severity == "Moderate":
        return {
            "Recovery": "80%",
            "ICU": "Not Required",
            "Stay": "3-5 Days"
        }

    else:
        return {
            "Recovery": "95%",
            "ICU": "Not Required",
            "Stay": "1-2 Days"
        }