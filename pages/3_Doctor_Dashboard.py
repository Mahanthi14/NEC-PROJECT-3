import streamlit as st
import pandas as pd
from utils.charts import disease_distribution_chart

st.set_page_config(page_title="Doctor Dashboard", page_icon="🩺", layout="wide")

st.title("🩺 Doctor Dashboard")
st.write("Doctor overview for today's patients, pending reports, predictions, and treatment recommendations.")

st.markdown("---")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Today's Patients", "12")
c2.metric("Pending Reports", "5")
c3.metric("High Risk Cases", "3")
c4.metric("Completed Appointments", "9")

st.markdown("---")

st.subheader("👥 Today's Patient List")

patients = pd.DataFrame({
    "Patient ID": ["P001", "P002", "P003"],
    "Name": ["Ravi Kumar", "Anitha", "Suresh"],
    "Age": [45, 32, 58],
    "Condition": ["Diabetes", "Fever", "Heart Risk"],
    "Risk Level": ["Medium", "Low", "High"]
})

st.dataframe(patients, use_container_width=True)

st.markdown("---")

st.subheader("📅 New Appointment Requests")

try:
    appointments = pd.read_csv("datasets/appointments.csv")
    st.dataframe(appointments.tail(10), use_container_width=True)
except Exception:
    st.warning("No appointments found.")

st.markdown("---")

st.subheader("💊 Treatment Recommendations")
st.info("P001 Ravi Kumar: Monitor sugar levels and continue prescribed medication.")
st.warning("P003 Suresh: Immediate cardiology review recommended.")

st.markdown("---")

st.subheader("📊 Disease Distribution Analytics")
st.plotly_chart(disease_distribution_chart(), use_container_width=True)