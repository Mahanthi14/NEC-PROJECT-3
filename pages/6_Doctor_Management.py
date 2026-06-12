import streamlit as st
import pandas as pd

st.set_page_config(page_title="Doctor Management", page_icon="🩺", layout="wide")

st.title("🩺 Doctor Management Module")
st.write("Doctor profiles, specialization, availability schedule, appointment management, and patient history access.")

tab1, tab2, tab3 = st.tabs(["➕ Add Doctor", "📋 Doctor Records", "📅 Availability"])

with tab1:
    col1, col2 = st.columns(2)

    with col1:
        doctor_id = st.text_input("Doctor ID")
        name = st.text_input("Doctor Name")
        department = st.selectbox("Department", ["Cardiology", "Neurology", "General Medicine", "Emergency", "Pediatrics"])

    with col2:
        specialization = st.text_input("Specialization")
        experience = st.number_input("Experience", min_value=0, max_value=50)
        qualification = st.text_input("Qualification")

    slots = st.multiselect("Available Slots", ["09:00 AM", "10:00 AM", "11:00 AM", "02:00 PM", "03:00 PM", "05:00 PM"])

    if st.button("Save Doctor", use_container_width=True):
        st.success("Doctor details saved successfully!")

with tab2:
    df = pd.DataFrame({
        "Doctor ID": ["D001", "D002", "D003"],
        "Name": ["Dr. Kiran", "Dr. Meena", "Dr. Arjun"],
        "Department": ["Cardiology", "General Medicine", "Emergency"],
        "Experience": [12, 8, 10],
        "Qualification": ["MD", "MBBS MD", "MD Emergency"]
    })

    st.dataframe(df, use_container_width=True)

with tab3:
    doctor = st.selectbox("Select Doctor", ["Dr. Kiran", "Dr. Meena", "Dr. Arjun"])
    st.success(f"{doctor} is available for selected slots.")
    st.info("Doctors can access assigned patient history and treatment records.")