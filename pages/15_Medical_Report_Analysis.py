import streamlit as st

st.set_page_config(page_title="Medical Report Analysis", page_icon="🧪", layout="wide")

st.title("🧪 Medical Report Analysis")
st.write("Analyze lab reports, detect abnormal values, and generate risk alerts.")

report_type = st.selectbox(
    "Select Report Type",
    ["Blood Test", "ECG", "MRI", "CT Scan", "X-Ray"]
)

uploaded_file = st.file_uploader(
    "Upload Medical Report",
    type=["pdf", "png", "jpg", "jpeg"]
)

st.subheader("Lab Parameters")

hemoglobin = st.number_input("Hemoglobin", value=13.0)
sugar = st.number_input("Blood Sugar", value=100)
cholesterol = st.number_input("Cholesterol", value=180)

if st.button("Analyze Report", use_container_width=True):

    if sugar > 180:
        st.error("High Blood Sugar Detected")

    if cholesterol > 240:
        st.warning("High Cholesterol Detected")

    if hemoglobin < 10:
        st.warning("Low Hemoglobin Detected")

    st.success("Analysis Completed")