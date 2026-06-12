import streamlit as st
import pandas as pd

st.set_page_config(page_title="Reporting Module", page_icon="📄", layout="wide")

st.title("📄 Reporting Module")

report = st.selectbox(
    "Select Report",
    [
        "Disease Statistics",
        "Resource Usage",
        "Bed Occupancy",
        "Doctor Performance",
        "Patient Recovery"
    ]
)

if st.button("Generate Report", use_container_width=True):

    st.success(f"{report} Generated Successfully")

    df = pd.DataFrame({
        "Metric": ["Value 1", "Value 2", "Value 3"],
        "Data": [100, 200, 300]
    })

    st.dataframe(df, use_container_width=True)

    csv = df.to_csv(index=False)

    st.download_button(
        "Download Report",
        csv,
        "report.csv",
        "text/csv"
    )