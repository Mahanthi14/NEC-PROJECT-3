import streamlit as st

st.set_page_config(
    page_title="Treatment Recommendation",
    page_icon="💊",
    layout="wide"
)

st.title("💊 Treatment Recommendation Engine")
st.write(
    "Suggest treatment plans, specialists, diagnostic tests, medication guidance, "
    "and priority level based on predicted disease and severity."
)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    patient_name = st.text_input("Patient Name")
    age = st.number_input("Age", min_value=1, max_value=120, value=35)
    disease = st.selectbox(
        "Predicted Disease",
        [
            "Diabetes",
            "Heart Disease",
            "Kidney Disease",
            "Cancer Risk",
            "Hypertension",
            "Asthma",
            "General Fever"
        ]
    )

with col2:
    severity = st.selectbox("Severity Level", ["Low", "Moderate", "High", "Critical"])
    symptoms = st.text_area("Patient Symptoms")
    allergies = st.text_input("Known Allergies")

st.markdown("---")

if st.button("Generate Treatment Recommendation", use_container_width=True):

    st.subheader("🧠 AI-Based Treatment Recommendation")

    if disease == "Diabetes":
        specialist = "Endocrinologist"
        tests = ["HbA1c Test", "Fasting Blood Sugar", "Lipid Profile", "Kidney Function Test"]
        plan = [
            "Follow a low-sugar diet",
            "Monitor blood glucose regularly",
            "Maintain daily physical activity",
            "Take prescribed diabetes medication"
        ]
        medication = "Metformin or insulin guidance as advised by doctor"

    elif disease == "Heart Disease":
        specialist = "Cardiologist"
        tests = ["ECG", "2D Echo", "Lipid Profile", "Stress Test"]
        plan = [
            "Monitor blood pressure regularly",
            "Reduce salt and oily food intake",
            "Avoid heavy physical strain",
            "Follow cardiac diet and medication schedule"
        ]
        medication = "BP tablets, blood thinners, or statins as prescribed"

    elif disease == "Kidney Disease":
        specialist = "Nephrologist"
        tests = ["Creatinine Test", "Urea Test", "Urine Analysis", "Kidney Function Test"]
        plan = [
            "Maintain controlled fluid intake",
            "Reduce salt intake",
            "Monitor kidney parameters",
            "Avoid unnecessary painkiller usage"
        ]
        medication = "Kidney-safe medication only under doctor supervision"

    elif disease == "Cancer Risk":
        specialist = "Oncologist"
        tests = ["Biopsy", "CT Scan", "MRI", "Tumor Marker Test"]
        plan = [
            "Immediate specialist consultation",
            "Further diagnostic screening",
            "Regular monitoring",
            "Follow oncologist treatment plan"
        ]
        medication = "Medication depends on confirmed diagnosis"

    elif disease == "Hypertension":
        specialist = "General Physician / Cardiologist"
        tests = ["BP Monitoring", "ECG", "Lipid Profile", "Kidney Function Test"]
        plan = [
            "Reduce salt intake",
            "Manage stress",
            "Regular BP monitoring",
            "Daily walking or light exercise"
        ]
        medication = "Antihypertensive medication as prescribed"

    elif disease == "Asthma":
        specialist = "Pulmonologist"
        tests = ["Pulmonary Function Test", "Chest X-Ray", "Oxygen Saturation Test"]
        plan = [
            "Avoid dust and pollution exposure",
            "Use inhaler as prescribed",
            "Monitor breathing difficulty",
            "Keep emergency inhaler available"
        ]
        medication = "Inhaler or bronchodilator as prescribed"

    else:
        specialist = "General Physician"
        tests = ["CBC", "Fever Profile", "CRP Test"]
        plan = [
            "Take rest",
            "Drink enough water",
            "Monitor temperature",
            "Take prescribed medication"
        ]
        medication = "Paracetamol or antibiotics only if prescribed"

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Recommended Specialist", specialist)

    with c2:
        st.metric("Severity", severity)

    with c3:
        if severity in ["High", "Critical"]:
            st.metric("Priority", "Emergency")
        elif severity == "Moderate":
            st.metric("Priority", "Within 24-48 hrs")
        else:
            st.metric("Priority", "Routine Checkup")

    st.markdown("---")

    st.subheader("🧪 Recommended Diagnostic Tests")
    for test in tests:
        st.write(f"✅ {test}")

    st.subheader("📋 Treatment Plan")
    for item in plan:
        st.write(f"• {item}")

    st.subheader("💊 Medication Guidance")
    st.info(medication)

    if allergies:
        st.warning(f"Allergy Alert: Patient has allergy information - {allergies}")

    if severity == "Critical":
        st.error("Critical case: Immediate doctor attention required.")
    elif severity == "High":
        st.warning("High severity: Schedule consultation as soon as possible.")
    elif severity == "Moderate":
        st.info("Moderate severity: Follow-up within 24-48 hours.")
    else:
        st.success("Low severity: Routine monitoring recommended.")