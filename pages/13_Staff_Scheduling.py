import streamlit as st
import pandas as pd

st.set_page_config(page_title="Staff Scheduling", page_icon="👨‍⚕️", layout="wide")

st.title("👨‍⚕️ Staff Scheduling Optimization")
st.write("Doctor shift management, nurse allocation, emergency staff planning, and AI-based peak load prediction.")

c1, c2, c3 = st.columns(3)
c1.metric("Doctors On Duty", "18")
c2.metric("Nurses On Duty", "42")
c3.metric("Emergency Staff", "12")

st.markdown("---")

tab1, tab2 = st.tabs(["📅 Shift Schedule", "🤖 AI Staff Suggestion"])

with tab1:
    df = pd.DataFrame({
        "Staff Name": ["Dr. Kiran", "Dr. Meena", "Nurse Anjali", "Nurse Priya", "Tech Ravi"],
        "Role": ["Doctor", "Doctor", "Nurse", "Nurse", "Technician"],
        "Department": ["Cardiology", "General", "ICU", "Emergency", "Lab"],
        "Shift": ["Morning", "Evening", "Night", "Morning", "Evening"]
    })

    st.dataframe(df, use_container_width=True)

with tab2:
    patient_load = st.slider("Expected Patient Load", 0, 500, 220)
    emergency_cases = st.slider("Expected Emergency Cases", 0, 100, 20)

    if st.button("Generate Staff Schedule Suggestion", use_container_width=True):
        doctors_needed = max(5, patient_load // 25)
        nurses_needed = max(10, patient_load // 12)
        emergency_staff = max(3, emergency_cases // 5)

        st.success("AI Staff Schedule Recommendation Generated")
        st.write(f"Doctors Needed: {doctors_needed}")
        st.write(f"Nurses Needed: {nurses_needed}")
        st.write(f"Emergency Staff Needed: {emergency_staff}")