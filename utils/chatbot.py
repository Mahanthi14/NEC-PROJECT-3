def chatbot_response(message):

    msg = message.lower()

    if "diabetes" in msg:
        return "Monitor sugar levels regularly."

    elif "heart" in msg:
        return "Consult a cardiologist."

    elif "appointment" in msg:
        return "Please use Appointment Module."

    return "Please consult a healthcare professional."