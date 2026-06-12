import streamlit as st
import pandas as pd

st.set_page_config(page_title="Bed Management", page_icon="🛏️", layout="wide")

st.title("🛏️ Bed Management System")
st.write("Real-time bed availability, ICU tracking, ward allocation, and emergency bed reservation.")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Beds", "150")
c2.metric("Available Beds", "68")
c3.metric("ICU Beds", "25")
c4.metric("Emergency Reserved", "10")

st.markdown("---")

tab1, tab2 = st.tabs(["🛏️ Bed Status", "🚨 Emergency Reservation"])

with tab1:
    df = pd.DataFrame({
        "Ward": ["General", "ICU", "Emergency", "Pediatric", "Maternity"],
        "Total Beds": [80, 25, 20, 15, 10],
        "Occupied": [50, 18, 12, 9, 6],
        "Available": [30, 7, 8, 6, 4]
    })

    st.dataframe(df, use_container_width=True)
    st.bar_chart(df.set_index("Ward")[["Occupied", "Available"]])

with tab2:
    patient = st.text_input("Patient Name")
    bed_type = st.selectbox("Required Bed Type", ["General", "ICU", "Emergency", "Pediatric"])
    priority = st.selectbox("Priority", ["Normal", "Urgent", "Critical"])

    if st.button("Reserve Bed", use_container_width=True):
        if priority == "Critical":
            st.error("Critical priority bed reserved immediately.")
        else:
            st.success("Bed reservation request submitted.")