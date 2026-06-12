import streamlit as st
import pandas as pd

st.set_page_config(page_title="Analytics Dashboard", page_icon="📊", layout="wide")

st.title("📊 Analytics Dashboard")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Patients", "245")
c2.metric("Doctors", "42")
c3.metric("Appointments", "620")
c4.metric("Recovery Rate", "91%")

disease = pd.DataFrame({
    "Disease": ["Diabetes", "Heart", "Kidney", "Cancer"],
    "Cases": [80, 55, 40, 20]
})

st.subheader("Disease Statistics")
st.bar_chart(disease.set_index("Disease"))

beds = pd.DataFrame({
    "Ward": ["General", "ICU", "Emergency"],
    "Occupied": [50, 18, 12]
})

st.subheader("Bed Occupancy")
st.bar_chart(beds.set_index("Ward"))