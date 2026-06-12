import streamlit as st

st.set_page_config(page_title="Notifications", page_icon="🔔", layout="wide")

st.title("🔔 Notification Module")

st.success("Appointment Reminder Sent")
st.info("Medicine Reminder Scheduled")
st.warning("Lab Report Available")
st.error("Emergency Alert Triggered")

st.subheader("Notification Channels")

st.checkbox("Email")
st.checkbox("SMS")
st.checkbox("WhatsApp")
st.checkbox("Push Notification")