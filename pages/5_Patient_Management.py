import streamlit as st
import pandas as pd

st.set_page_config(page_title="Patient Management", page_icon="👤", layout="wide")

st.title("👤 Patient Management Module")
st.write("Patient registration, personal details, medical history, allergies, previous treatments, lab reports, and insurance details.")

tab1, tab2, tab3 = st.tabs(["➕ Register Patient", "📋 Patient Records", "🏥 Medical History"])

with tab1:
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Patient Name", key="pm_name")
        age = st.number_input("Age", min_value=1, max_value=120, key="pm_age")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"], key="pm_gender")
        weight = st.number_input("Weight (kg)", min_value=1, key="pm_weight")
        blood_group = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"], key="pm_bg")

    with col2:
        height = st.number_input("Height (cm)", min_value=1, key="pm_height")
        phone = st.text_input("Phone Number", key="pm_phone")
        insurance = st.text_input("Insurance Details", key="pm_insurance")
        conditions = st.text_area("Medical Conditions", key="pm_conditions")
        family_history = st.text_area("Family History", key="pm_family")

    allergies = st.text_area("Allergies Information", key="pm_allergies")
    previous_treatments = st.text_area("Previous Treatments", key="pm_previous_treatments")

    if st.button("Save Patient", use_container_width=True, key="pm_save"):
        st.success("Patient registered successfully!")

with tab2:
    df = pd.DataFrame({
        "Patient ID": ["P001", "P002", "P003"],
        "Name": ["Ravi Kumar", "Anitha", "Suresh"],
        "Age": [45, 32, 58],
        "Gender": ["Male", "Female", "Male"],
        "Blood Group": ["O+", "A+", "B+"],
        "Condition": ["Diabetes", "Checkup", "Heart Risk"]
    })

    st.dataframe(df, use_container_width=True)

with tab3:
    patient = st.selectbox("Select Patient", ["Ravi Kumar", "Anitha", "Suresh"], key="pm_select_patient")
    st.info(f"Showing medical history for {patient}")

    st.text_area("Medical History", key="pm_medical_history")
    st.text_area("Previous Treatments", key="pm_history_previous_treatments")
    st.file_uploader("Upload Lab Report", type=["pdf", "png", "jpg", "jpeg"], key="pm_lab_upload")