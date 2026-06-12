import streamlit as st

st.set_page_config(page_title="Emergency Alert", page_icon="🚨", layout="wide")

st.title("🚨 Emergency Alert System")

oxygen = st.slider("Oxygen Level (%)", 50, 100, 96)
heart_rate = st.slider("Heart Rate", 40, 180, 80)
bp = st.slider("Blood Pressure", 70, 220, 120)

if st.button("Check Emergency Status", use_container_width=True):

    if oxygen < 90:
        st.error("🚨 Critical Alert")
        st.write("Doctor Notified")
        st.write("Nurse Notified")
        st.write("Family Alert Sent")

    elif heart_rate > 140:
        st.warning("⚠️ High Heart Rate Alert")

    else:
        st.success("Patient Stable")