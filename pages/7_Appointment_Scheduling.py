import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Appointment Scheduling", page_icon="📅", layout="wide")

CSV_PATH = "datasets/appointments.csv"

st.title("📅 Appointment Scheduling Module")

tab1, tab2 = st.tabs(["📌 Book Appointment", "📋 Appointment Records"])

with tab1:
    patient_id = st.text_input("Patient ID")
    doctor_id = st.text_input("Doctor ID")
    date = st.date_input("Appointment Date")
    time = st.selectbox("Time", ["09:00 AM", "10:00 AM", "11:00 AM", "02:00 PM", "03:00 PM"])
    reason = st.text_area("Reason", key="reason")

    if st.button("Confirm Appointment", use_container_width=True):
        df = pd.read_csv(CSV_PATH)

        new_id = f"A{len(df)+1:03d}"

        new_row = {
            "Appointment_ID": new_id,
            "Patient_ID": patient_id,
            "Doctor_ID": doctor_id,
            "Date": str(date),
            "Time": time,
            "Status": "Pending"
        }

        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(CSV_PATH, index=False)

        st.success("Appointment booked successfully! Doctor can now view it.")

with tab2:
    df = pd.read_csv(CSV_PATH)
    st.dataframe(df, use_container_width=True)