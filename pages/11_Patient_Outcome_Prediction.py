import streamlit as st

st.set_page_config(
    page_title="Patient Outcome Prediction",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Patient Outcome Prediction Module")
st.write("Predict recovery probability, ICU requirement, readmission risk, mortality risk, and expected hospital stay duration.")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    patient_name = st.text_input("Patient Name")
    age = st.number_input("Age", min_value=1, max_value=120, value=45)
    severity = st.selectbox("Disease Severity", ["Low", "Moderate", "High", "Critical"])
    oxygen = st.number_input("Oxygen Level (%)", min_value=0, max_value=100, value=96)

with col2:
    bp = st.number_input("Blood Pressure", min_value=0, max_value=250, value=120)
    sugar = st.number_input("Sugar Level", min_value=0, max_value=500, value=110)
    comorbidity = st.selectbox("Comorbidities Present", ["No", "Yes"])
    previous_admission = st.selectbox("Previous Hospital Admission", ["No", "Yes"])

if st.button("Predict Patient Outcome", use_container_width=True):

    risk = 0

    if age > 60:
        risk += 15
    if severity == "Moderate":
        risk += 20
    elif severity == "High":
        risk += 40
    elif severity == "Critical":
        risk += 60
    if oxygen < 92:
        risk += 20
    if bp > 150:
        risk += 10
    if sugar > 180:
        risk += 10
    if comorbidity == "Yes":
        risk += 15
    if previous_admission == "Yes":
        risk += 10

    recovery_probability = max(5, 100 - risk)
    readmission_risk = min(100, risk)
    mortality_risk = min(100, risk // 2)

    if severity == "Critical" or oxygen < 90:
        icu = "Required"
        stay = "10-15 Days"
    elif severity == "High":
        icu = "May be Required"
        stay = "7-10 Days"
    elif severity == "Moderate":
        icu = "Not Required"
        stay = "3-5 Days"
    else:
        icu = "Not Required"
        stay = "1-2 Days"

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Recovery Probability", f"{recovery_probability}%")
    c2.metric("ICU Requirement", icu)
    c3.metric("Readmission Risk", f"{readmission_risk}%")
    c4.metric("Expected Stay", stay)

    st.markdown("---")

    if mortality_risk >= 40:
        st.error(f"Mortality Risk Estimate: {mortality_risk}%")
        st.warning("Immediate doctor supervision required.")
    elif mortality_risk >= 20:
        st.warning(f"Mortality Risk Estimate: {mortality_risk}%")
        st.info("Close monitoring recommended.")
    else:
        st.success(f"Mortality Risk Estimate: {mortality_risk}%")
        st.info("Patient condition is comparatively stable.")