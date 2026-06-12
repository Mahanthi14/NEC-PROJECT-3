import streamlit as st
import pandas as pd

st.set_page_config(page_title="EHR Module", page_icon="📋", layout="wide")

st.title("📋 Electronic Health Record (EHR) Module")
st.write("Store medical records, prescriptions, diagnostic reports, treatment history, and vaccination records.")

tab1, tab2, tab3 = st.tabs(["📝 Medical Records", "💊 Prescriptions", "📂 Reports"])

with tab1:
    patient = st.selectbox("Select Patient", ["Ravi Kumar", "Anitha", "Suresh"])

    col1, col2 = st.columns(2)

    with col1:
        st.text_input("Blood Group", "O+")
        st.text_input("Primary Disease", "Diabetes")
        st.text_input("Allergies", "Penicillin")

    with col2:
        st.text_input("Insurance Provider", "Star Health")
        st.text_input("Emergency Contact", "9876543210")
        st.text_input("Vaccination Records", "COVID-19, Hepatitis B")

    st.text_area("Treatment History", "Patient has Type-2 Diabetes and hypertension.")

    if st.button("Save EHR", use_container_width=True):
        st.success("EHR record saved successfully!")

with tab2:
    prescriptions = pd.DataFrame({
        "Date": ["2026-06-01", "2026-06-05", "2026-06-10"],
        "Doctor": ["Dr. Kiran", "Dr. Meena", "Dr. Arjun"],
        "Medicine": ["Metformin", "Paracetamol", "Aspirin"],
        "Duration": ["30 Days", "5 Days", "15 Days"]
    })

    st.dataframe(prescriptions, use_container_width=True)

with tab3:
    report_type = st.selectbox("Report Type", ["Blood Test", "ECG", "MRI", "CT Scan", "X-Ray"])
    st.file_uploader("Upload Report", type=["pdf", "png", "jpg", "jpeg"])
    st.text_area("Doctor Remarks")

    if st.button("Save Report", use_container_width=True):
        st.success("Diagnostic report saved successfully!")