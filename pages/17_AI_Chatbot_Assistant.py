import streamlit as st

st.set_page_config(
    page_title="AI Healthcare Virtual Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Healthcare Virtual Assistant")

st.success("""
Hello! I am your AI Healthcare Assistant.

I can help you with:
• Disease Information
• Symptom Guidance
• Treatment Suggestions
• Specialist Recommendations
• Emergency Advice
• Appointment Assistance
""")

st.markdown("---")

st.subheader("💡 Frequently Asked Questions")

question = st.selectbox(
    "Choose a Question",
    [
        "What are symptoms of diabetes?",
        "What are symptoms of heart disease?",
        "How to control blood pressure?",
        "How to reduce cholesterol?",
        "Recommended tests for diabetes?",
        "Recommended tests for heart disease?",
        "What is normal oxygen level?",
        "What are asthma triggers?",
        "When is ICU required?",
        "Emergency warning signs?",
        "Which specialist should I consult?",
        "How can I book an appointment?"
    ]
)

if st.button("Get Answer", use_container_width=True):

    if question == "What are symptoms of diabetes?":
        st.info("""
        Common Diabetes Symptoms:

        • Frequent urination
        • Excessive thirst
        • Fatigue
        • Blurred vision
        • Slow wound healing
        • Unexplained weight loss
        """)

    elif question == "What are symptoms of heart disease?":
        st.info("""
        Common Heart Disease Symptoms:

        • Chest pain
        • Shortness of breath
        • Dizziness
        • Fatigue
        • Irregular heartbeat
        • Swelling in legs
        """)

    elif question == "How to control blood pressure?":
        st.info("""
        Blood Pressure Control Tips:

        • Reduce salt intake
        • Exercise regularly
        • Avoid smoking
        • Manage stress
        • Monitor BP frequently
        """)

    elif question == "How to reduce cholesterol?":
        st.info("""
        Cholesterol Reduction Tips:

        • Avoid fried foods
        • Increase fiber intake
        • Exercise daily
        • Maintain healthy weight
        • Follow doctor's advice
        """)

    elif question == "Recommended tests for diabetes?":
        st.info("""
        Diabetes Tests:

        • HbA1c Test
        • Fasting Blood Sugar
        • Postprandial Blood Sugar
        • Kidney Function Test
        """)

    elif question == "Recommended tests for heart disease?":
        st.info("""
        Heart Disease Tests:

        • ECG
        • Echo Test
        • Stress Test
        • Lipid Profile
        """)

    elif question == "What is normal oxygen level?":
        st.info("""
        Normal Oxygen Saturation:

        ✅ 95% - 100% : Normal

        ⚠️ 90% - 94% : Monitor Carefully

        🚨 Below 90% : Immediate Medical Attention Required
        """)

    elif question == "What are asthma triggers?":
        st.info("""
        Common Asthma Triggers:

        • Dust
        • Smoke
        • Pollen
        • Cold Air
        • Strong Odors
        """)

    elif question == "When is ICU required?":
        st.error("""
        ICU May Be Required When:

        • Oxygen Level < 90%
        • Severe Chest Pain
        • Organ Failure Risk
        • Critical Infection
        • Unstable Vital Signs
        """)

    elif question == "Emergency warning signs?":
        st.error("""
        Emergency Symptoms:

        • Severe Chest Pain
        • Difficulty Breathing
        • Loss of Consciousness
        • Stroke Symptoms
        • Severe Bleeding
        """)

    elif question == "Which specialist should I consult?":
        st.info("""
        Specialist Recommendations:

        Diabetes → Endocrinologist

        Heart Disease → Cardiologist

        Kidney Disease → Nephrologist

        Asthma → Pulmonologist

        Cancer Risk → Oncologist
        """)

    elif question == "How can I book an appointment?":
        st.success("""
        Steps:

        1. Open Appointment Scheduling Module

        2. Select Patient

        3. Select Doctor

        4. Choose Date & Time

        5. Confirm Appointment
        """)

st.markdown("---")

st.subheader("💬 Ask Your Own Question")

query = st.text_input("Type your healthcare question")

if st.button("Send", use_container_width=True):

    q = query.lower()

    if "diabetes" in q:
        st.success("""
        Diabetes is a chronic condition affecting blood sugar levels.

        Recommendations:
        • Healthy diet
        • Regular exercise
        • Monitor glucose levels
        • Follow doctor's advice
        """)

    elif "heart" in q:
        st.success("""
        Heart health recommendations:

        • Reduce cholesterol
        • Exercise regularly
        • Avoid smoking
        • Monitor BP
        • Consult a cardiologist
        """)

    elif "appointment" in q:
        st.success("""
        Please visit the Appointment Scheduling Module to book an appointment.
        """)

    elif "medicine" in q:
        st.warning("""
        Always consult your doctor before taking any medication.
        """)

    elif "oxygen" in q:
        st.info("""
        Oxygen below 90% may require immediate medical attention.
        """)

    elif "bp" in q or "blood pressure" in q:
        st.info("""
        Normal Blood Pressure is around 120/80 mmHg.
        """)

    else:
        st.info("""
        I can help with:
        • Diabetes
        • Heart Disease
        • Blood Pressure
        • Cholesterol
        • Appointments
        • Emergency Guidance
        • Specialist Recommendations
        """)