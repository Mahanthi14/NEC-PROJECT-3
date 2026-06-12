import streamlit as st
import pandas as pd
from utils.charts import appointment_status_chart

st.set_page_config(page_title="Patient Dashboard", page_icon="👤", layout="wide")

st.title("👤 Patient Dashboard")
st.write("Patient health overview, appointments, reports, prescriptions, and health trends.")

st.markdown("---")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Appointments", "4")
c2.metric("Reports", "8")
c3.metric("Prescriptions", "5")
c4.metric("Health Score", "92%")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📅 Upcoming Appointments")
    st.info("Dr. Kiran - Cardiology | 15 June 2026 | 10:00 AM")
    st.info("Dr. Meena - General Medicine | 18 June 2026 | 02:00 PM")

with col2:
    st.subheader("📋 Recent Reports")
    st.success("Blood Test - Normal")
    st.warning("Cholesterol - Slightly High")
    st.success("ECG - Normal")

st.markdown("---")

st.subheader("📈 Health Trends")

df = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Sugar Level": [98, 110, 105, 118, 102],
    "BP Level": [120, 118, 122, 121, 119]
})

st.line_chart(df.set_index("Day"))

st.markdown("---")

st.subheader("📊 Appointment Status Analytics")
st.plotly_chart(appointment_status_chart(), use_container_width=True)