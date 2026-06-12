import streamlit as st
import pandas as pd

st.set_page_config(page_title="Resource Allocation", page_icon="🏥", layout="wide")

st.title("🏥 Resource Allocation Module")
st.write("Beds, ventilators, oxygen units, medical equipment, demand forecasting, and utilization analysis.")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Ventilators", "15 / 20")
c2.metric("Oxygen Units", "50 / 60")
c3.metric("Monitors", "35 / 45")
c4.metric("Wheelchairs", "25 / 30")

st.markdown("---")

df = pd.DataFrame({
    "Resource": ["Beds", "Ventilators", "Oxygen Units", "Monitors", "Wheelchairs"],
    "Available Units": [68, 15, 50, 35, 25],
    "Total Units": [150, 20, 60, 45, 30]
})

st.subheader("📊 Resource Utilization")
st.dataframe(df, use_container_width=True)

df["Utilization %"] = ((df["Total Units"] - df["Available Units"]) / df["Total Units"]) * 100
st.bar_chart(df.set_index("Resource")["Utilization %"])

st.subheader("🤖 AI Resource Allocation Recommendation")

patient_inflow = st.slider("Expected Patient Inflow", 0, 500, 200)

if st.button("Generate Resource Recommendation", use_container_width=True):
    if patient_inflow > 300:
        st.error("High demand expected. Increase ICU beds, oxygen units, and emergency staff.")
    elif patient_inflow > 150:
        st.warning("Moderate demand expected. Monitor bed and oxygen usage.")
    else:
        st.success("Resource availability is sufficient for expected demand.")