from pathlib import Path

def write(path, code):
    Path(path).write_text(code, encoding="utf-8")

# 1. charts.py
write("utils/charts.py", r'''
import pandas as pd
import plotly.express as px

def age_distribution_chart():
    df = pd.DataFrame({"Age Group":["0-20","21-40","41-60","60+"],"Patients":[12,28,35,18]})
    return px.bar(df, x="Age Group", y="Patients", title="Patient Age Distribution")

def doctor_department_chart():
    df = pd.DataFrame({"Department":["Cardiology","General","Emergency","Neurology","Orthopedics"],"Doctors":[18,25,15,12,10]})
    return px.pie(df, names="Department", values="Doctors", title="Department-wise Doctors")

def appointment_status_chart():
    df = pd.DataFrame({"Status":["Approved","Pending","Completed","Rescheduled"],"Count":[25,12,10,3]})
    return px.pie(df, names="Status", values="Count", title="Appointment Status")

def ehr_report_chart():
    df = pd.DataFrame({"Report Type":["Blood Test","ECG","MRI","CT Scan","X-Ray"],"Count":[30,18,8,10,14]})
    return px.bar(df, x="Report Type", y="Count", title="EHR Report Analysis")

def risk_score_chart():
    df = pd.DataFrame({"Risk":["Low","Medium","High"],"Cases":[35,20,12]})
    return px.bar(df, x="Risk", y="Cases", title="Disease Risk Score Distribution")

def treatment_chart():
    df = pd.DataFrame({"Specialist":["Cardiologist","Endocrinologist","Nephrologist","Pulmonologist","Physician"],"Cases":[28,35,14,18,22]})
    return px.bar(df, x="Specialist", y="Cases", title="Specialist Recommendation Analytics")

def outcome_chart():
    df = pd.DataFrame({"Category":["Recovery","Readmission","Mortality"],"Percentage":[85,22,8]})
    return px.bar(df, x="Category", y="Percentage", title="Patient Outcome Prediction Analytics")

def bed_occupancy_chart():
    df = pd.DataFrame({"Ward":["General","ICU","Emergency","Pediatric","Maternity"],"Occupied":[50,18,12,9,6],"Available":[30,7,8,6,4]})
    return px.bar(df, x="Ward", y=["Occupied","Available"], title="Bed Occupancy Analysis")

def staff_shift_chart():
    df = pd.DataFrame({"Shift":["Morning","Evening","Night"],"Staff Count":[45,38,30]})
    return px.bar(df, x="Shift", y="Staff Count", title="Staff Shift Allocation")

def resource_utilization_chart():
    df = pd.DataFrame({"Resource":["Ventilators","Oxygen Units","Monitors","Wheelchairs","ICU Beds"],"Utilization":[75,83,70,60,88]})
    return px.line(df, x="Resource", y="Utilization", markers=True, title="Resource Utilization Trend")

def report_risk_chart():
    df = pd.DataFrame({"Risk Level":["Low","Medium","High"],"Reports":[25,15,10]})
    return px.pie(df, names="Risk Level", values="Reports", title="Medical Report Risk Analysis")

def notification_chart():
    df = pd.DataFrame({"Notification":["Appointment","Medicine","Emergency","Lab Report"],"Count":[40,28,12,22]})
    return px.bar(df, x="Notification", y="Count", title="Notification Analytics")
''')

# 5 Patient Management
write("pages/5_Patient_Management.py", r'''
import streamlit as st
import pandas as pd
from utils.charts import age_distribution_chart

st.set_page_config(page_title="Patient Management", page_icon="👤", layout="wide")
st.title("👤 Patient Management Module")
st.write("Patient registration, personal details, medical history, allergies, previous treatments, lab reports, and insurance details.")

tab1, tab2, tab3, tab4 = st.tabs(["➕ Register Patient","📋 Patient Records","🏥 Medical History","📊 Analytics"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Patient Name", key="p_name")
        st.number_input("Age", min_value=1, max_value=120, key="p_age")
        st.selectbox("Gender", ["Male","Female","Other"], key="p_gender")
        st.number_input("Weight (kg)", min_value=1, key="p_weight")
        st.selectbox("Blood Group", ["A+","A-","B+","B-","O+","O-","AB+","AB-"], key="p_bg")
    with col2:
        st.number_input("Height (cm)", min_value=1, key="p_height")
        st.text_input("Phone Number", key="p_phone")
        st.text_input("Insurance Details", key="p_insurance")
        st.text_area("Medical Conditions", key="p_conditions")
        st.text_area("Family History", key="p_family")
    st.text_area("Allergies Information", key="p_allergy")
    st.text_area("Previous Treatments", key="p_treatments")
    if st.button("Save Patient", use_container_width=True):
        st.success("Patient registered successfully!")

with tab2:
    df = pd.read_csv("datasets/patients.csv")
    st.dataframe(df, use_container_width=True)

with tab3:
    st.selectbox("Select Patient", ["Ravi Kumar","Anitha Reddy","Suresh Babu"], key="p_select")
    st.text_area("Medical History", key="p_med_history")
    st.text_area("Previous Treatments", key="p_prev_history")
    st.file_uploader("Upload Lab Report", type=["pdf","png","jpg","jpeg"], key="p_upload")

with tab4:
    st.plotly_chart(age_distribution_chart(), use_container_width=True)
''')

# 6 Doctor Management
write("pages/6_Doctor_Management.py", r'''
import streamlit as st
import pandas as pd
from utils.charts import doctor_department_chart

st.set_page_config(page_title="Doctor Management", page_icon="🩺", layout="wide")
st.title("🩺 Doctor Management Module")
st.write("Doctor profile, specialization, availability schedule, appointment management, and patient history access.")

tab1, tab2, tab3 = st.tabs(["➕ Add Doctor","📋 Doctor Records","📊 Department Analytics"])

with tab1:
    c1, c2 = st.columns(2)
    with c1:
        st.text_input("Doctor ID")
        st.text_input("Doctor Name")
        st.selectbox("Department", ["Cardiology","Neurology","General Medicine","Emergency","Pediatrics"])
    with c2:
        st.text_input("Specialization")
        st.number_input("Experience", min_value=0, max_value=50)
        st.text_input("Qualification")
    st.multiselect("Available Slots", ["09 AM","10 AM","11 AM","02 PM","03 PM","05 PM"])
    if st.button("Save Doctor", use_container_width=True):
        st.success("Doctor details saved successfully!")

with tab2:
    df = pd.read_csv("datasets/doctors.csv")
    st.dataframe(df, use_container_width=True)

with tab3:
    st.plotly_chart(doctor_department_chart(), use_container_width=True)
''')

# 7 Appointment Scheduling
write("pages/7_Appointment_Scheduling.py", r'''
import streamlit as st
import pandas as pd
from utils.charts import appointment_status_chart

st.set_page_config(page_title="Appointment Scheduling", page_icon="📅", layout="wide")
st.title("📅 Appointment Scheduling Module")

APPOINTMENTS = "datasets/appointments.csv"
patients_df = pd.read_csv("datasets/patients.csv")
doctors_df = pd.read_csv("datasets/doctors.csv")

tab1, tab2, tab3 = st.tabs(["📌 Book Appointment","📋 Appointment Records","📊 Analytics"])

with tab1:
    patient_name = st.selectbox("Select Patient", patients_df["Name"].tolist())
    doctor_name = st.selectbox("Select Doctor", doctors_df["Name"].tolist())

    patient_id = patients_df.loc[patients_df["Name"] == patient_name, "Patient_ID"].values[0]
    doctor_id = doctors_df.loc[doctors_df["Name"] == doctor_name, "Doctor_ID"].values[0]

    c1, c2 = st.columns(2)
    with c1:
        st.info(f"Patient ID: {patient_id}")
        date = st.date_input("Appointment Date")
    with c2:
        st.info(f"Doctor ID: {doctor_id}")
        time = st.selectbox("Time", ["09:00 AM","10:00 AM","11:00 AM","02:00 PM","03:00 PM"])

    st.text_area("Reason for Visit", key="reason_visit")

    if st.button("Confirm Appointment", use_container_width=True):
        df = pd.read_csv(APPOINTMENTS)
        new_id = f"A{len(df)+1:03d}"
        new_row = {"Appointment_ID":new_id,"Patient_ID":patient_id,"Doctor_ID":doctor_id,"Date":str(date),"Time":time,"Status":"Pending"}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(APPOINTMENTS, index=False)
        st.success(f"Appointment booked successfully! ID: {new_id}")

with tab2:
    st.dataframe(pd.read_csv(APPOINTMENTS), use_container_width=True)

with tab3:
    st.plotly_chart(appointment_status_chart(), use_container_width=True)
''')

# 8 EHR
write("pages/8_EHR_Module.py", r'''
import streamlit as st
import pandas as pd
from utils.charts import ehr_report_chart

st.set_page_config(page_title="EHR Module", page_icon="📋", layout="wide")
st.title("📋 Electronic Health Record Module")

tab1, tab2, tab3 = st.tabs(["📝 EHR Records","📂 Reports","📊 Analytics"])

with tab1:
    df = pd.read_csv("datasets/ehr_records.csv")
    st.dataframe(df, use_container_width=True)

with tab2:
    st.selectbox("Report Type", ["Blood Test","ECG","MRI","CT Scan","X-Ray"])
    st.file_uploader("Upload Report", type=["pdf","png","jpg","jpeg"], key="ehr_upload")
    st.text_area("Doctor Remarks", key="ehr_remarks")
    if st.button("Save Report", use_container_width=True):
        st.success("Report saved successfully!")

with tab3:
    st.plotly_chart(ehr_report_chart(), use_container_width=True)
''')

# 9 add graph part in AI page lightly
# 10 Treatment
write("pages/10_Treatment_Recommendation.py", r'''
import streamlit as st
from utils.charts import treatment_chart

st.set_page_config(page_title="Treatment Recommendation", page_icon="💊", layout="wide")
st.title("💊 Treatment Recommendation Engine")

disease = st.selectbox("Predicted Disease", ["Diabetes","Heart Disease","Kidney Disease","Cancer Risk","Hypertension","Asthma","General Fever"])
severity = st.selectbox("Severity Level", ["Low","Moderate","High","Critical"])

if st.button("Generate Treatment Recommendation", use_container_width=True):
    st.success(f"Treatment plan generated for {disease}")
    st.info("Specialist, tests, medication guidance and priority recommendations displayed.")

st.markdown("---")
st.subheader("📊 Specialist Recommendation Analytics")
st.plotly_chart(treatment_chart(), use_container_width=True)
''')

# 11 Outcome
write("pages/11_Patient_Outcome_Prediction.py", r'''
import streamlit as st
from utils.charts import outcome_chart

st.set_page_config(page_title="Patient Outcome Prediction", page_icon="📈", layout="wide")
st.title("📈 Patient Outcome Prediction Module")

age = st.number_input("Age", 1, 120, 45)
severity = st.selectbox("Disease Severity", ["Low","Moderate","High","Critical"])
oxygen = st.number_input("Oxygen Level (%)", 0, 100, 96)

if st.button("Predict Outcome", use_container_width=True):
    st.metric("Recovery Probability", "85%")
    st.metric("ICU Requirement", "Not Required")
    st.metric("Expected Stay", "3-5 Days")

st.markdown("---")
st.plotly_chart(outcome_chart(), use_container_width=True)
''')

# 12 Bed
write("pages/12_Bed_Management.py", r'''
import streamlit as st
import pandas as pd
from utils.charts import bed_occupancy_chart

st.set_page_config(page_title="Bed Management", page_icon="🛏️", layout="wide")
st.title("🛏️ Bed Management System")

df = pd.read_csv("datasets/beds.csv")
st.dataframe(df, use_container_width=True)

st.markdown("---")
st.plotly_chart(bed_occupancy_chart(), use_container_width=True)
''')

# 13 Staff
write("pages/13_Staff_Scheduling.py", r'''
import streamlit as st
import pandas as pd
from utils.charts import staff_shift_chart

st.set_page_config(page_title="Staff Scheduling", page_icon="👨‍⚕️", layout="wide")
st.title("👨‍⚕️ Staff Scheduling Optimization")

df = pd.read_csv("datasets/staff.csv")
st.dataframe(df, use_container_width=True)

st.markdown("---")
st.plotly_chart(staff_shift_chart(), use_container_width=True)
''')

# 14 Resource
write("pages/14_Resource_Allocation.py", r'''
import streamlit as st
import pandas as pd
from utils.charts import resource_utilization_chart

st.set_page_config(page_title="Resource Allocation", page_icon="⚙️", layout="wide")
st.title("⚙️ Resource Allocation Module")

df = pd.read_csv("datasets/resources.csv")
st.dataframe(df, use_container_width=True)

st.markdown("---")
st.plotly_chart(resource_utilization_chart(), use_container_width=True)
''')

# 15 Medical Report
write("pages/15_Medical_Report_Analysis.py", r'''
import streamlit as st
import pandas as pd
from utils.charts import report_risk_chart

st.set_page_config(page_title="Medical Report Analysis", page_icon="🧪", layout="wide")
st.title("🧪 Medical Report Analysis")

df = pd.read_csv("datasets/medical_reports.csv")
st.dataframe(df, use_container_width=True)

st.markdown("---")
st.plotly_chart(report_risk_chart(), use_container_width=True)
''')

# 18 Analytics
write("pages/18_Analytics_Dashboard.py", r'''
import streamlit as st
from utils.charts import disease_distribution_chart, bed_occupancy_chart, resource_utilization_chart, report_risk_chart

st.set_page_config(page_title="Analytics Dashboard", page_icon="📊", layout="wide")
st.title("📊 Analytics Dashboard")

c1,c2,c3,c4 = st.columns(4)
c1.metric("Patients","1250")
c2.metric("Doctors","120")
c3.metric("Appointments","620")
c4.metric("Recovery Rate","91%")

st.plotly_chart(disease_distribution_chart(), use_container_width=True)
st.plotly_chart(bed_occupancy_chart(), use_container_width=True)
st.plotly_chart(resource_utilization_chart(), use_container_width=True)
st.plotly_chart(report_risk_chart(), use_container_width=True)
''')

# 19 Notifications
write("pages/19_Notifications.py", r'''
import streamlit as st
from utils.charts import notification_chart

st.set_page_config(page_title="Notifications", page_icon="🔔", layout="wide")
st.title("🔔 Notification Module")

st.success("Appointment Reminder Sent")
st.info("Medicine Reminder Scheduled")
st.warning("Lab Report Available")
st.error("Emergency Alert Triggered")

st.markdown("---")
st.plotly_chart(notification_chart(), use_container_width=True)
''')

# 20 Reports
write("pages/20_Reporting_Module.py", r'''
import streamlit as st
import pandas as pd
from utils.charts import disease_distribution_chart, report_risk_chart

st.set_page_config(page_title="Reporting Module", page_icon="📄", layout="wide")
st.title("📄 Reporting Module")

report = st.selectbox("Select Report", ["Disease Statistics","Resource Usage","Bed Occupancy","Doctor Performance","Patient Recovery"])

if st.button("Generate Report", use_container_width=True):
    df = pd.DataFrame({"Metric":["Value 1","Value 2","Value 3"],"Data":[100,200,300]})
    st.dataframe(df, use_container_width=True)
    st.download_button("Download Report", df.to_csv(index=False), "report.csv", "text/csv")

st.markdown("---")
st.plotly_chart(disease_distribution_chart(), use_container_width=True)
st.plotly_chart(report_risk_chart(), use_container_width=True)
''')

print("Graphs added successfully to major pages.")