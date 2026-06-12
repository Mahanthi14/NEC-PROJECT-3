import streamlit as st
import pandas as pd
from utils.charts import disease_distribution_chart, bed_occupancy_chart, resource_utilization_chart

st.set_page_config(page_title="Admin Dashboard", page_icon="🏥", layout="wide")

st.title("🏥 Admin Dashboard")
st.write("Hospital resource utilization, bed occupancy, staff performance, and analytics overview.")

st.markdown("---")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Patients", "1,250", "+12%")
c2.metric("Doctors", "120", "+5")
c3.metric("Available Beds", "230", "-15")
c4.metric("Resource Usage", "76%", "+8%")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Disease Distribution")
    st.plotly_chart(disease_distribution_chart(), use_container_width=True)

with col2:
    st.subheader("🛏️ Bed Occupancy")
    st.plotly_chart(bed_occupancy_chart(), use_container_width=True)

st.markdown("---")

st.subheader("⚙️ Resource Utilization")
st.plotly_chart(resource_utilization_chart(), use_container_width=True)

st.markdown("---")

st.subheader("👨‍⚕️ Staff Performance")

staff = pd.DataFrame({
    "Staff": ["Doctors", "Nurses", "Technicians", "Support Staff"],
    "Count": [120, 240, 80, 150],
    "Efficiency": ["95%", "89%", "84%", "81%"]
})

st.dataframe(staff, use_container_width=True)

st.success("AI Insight: ICU occupancy may increase by 15% this week. Additional staff allocation recommended.")