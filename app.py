import streamlit as st
from utils.database import create_tables, insert_default_users
from utils.auth import login_user

st.set_page_config(
    page_title="AI Healthcare System",
    page_icon="🏥",
    layout="wide"
)

create_tables()
insert_default_users()

st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: #0d6efd;
}
.sub-title {
    text-align: center;
    font-size: 18px;
    color: #475569;
    margin-bottom: 30px;
}
.module-card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0px 4px 16px rgba(0,0,0,0.10);
    margin-bottom: 18px;
    border-left: 6px solid #0d6efd;
}
.module-title {
    font-size: 20px;
    font-weight: 700;
    color: #0f172a;
}
.module-desc {
    font-size: 14px;
    color: #64748b;
}
.login-box {
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0px 6px 25px rgba(0,0,0,0.12);
}
</style>
""", unsafe_allow_html=True)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None
    st.session_state.username = None

modules = [
    ("🔐", "Authentication", "Secure role-based login for Patient, Doctor and Admin.", "pages/1_Authentication.py"),
    ("👤", "Patient Dashboard", "Health trends, reports, prescriptions and appointments.", "pages/2_Patient_Dashboard.py"),
    ("🩺", "Doctor Dashboard", "Today's patients, pending reports and recommendations.", "pages/3_Doctor_Dashboard.py"),
    ("🏥", "Admin Dashboard", "Hospital resources, analytics and performance overview.", "pages/4_Admin_Dashboard.py"),
    ("📋", "Patient Management", "Patient registration, history, allergies and insurance details.", "pages/5_Patient_Management.py"),
    ("🩺", "Doctor Management", "Doctor profiles, departments, schedules and availability.", "pages/6_Doctor_Management.py"),
    ("📅", "Appointment Scheduling", "Online booking, approvals and appointment tracking.", "pages/7_Appointment_Scheduling.py"),
    ("📁", "EHR Module", "Medical records, prescriptions, reports and vaccination history.", "pages/8_EHR_Module.py"),
    ("🤖", "AI Disease Prediction", "Diabetes and heart disease prediction using ML models.", "pages/9_AI_Disease_Prediction.py"),
    ("💊", "Treatment Recommendation", "Suggest specialists, tests and treatment plans.", "pages/10_Treatment_Recommendation.py"),
    ("📈", "Patient Outcome Prediction", "Recovery probability, ICU need and stay duration.", "pages/11_Patient_Outcome_Prediction.py"),
    ("🛏️", "Bed Management", "Real-time bed availability and ICU tracking.", "pages/12_Bed_Management.py"),
    ("👨‍⚕️", "Staff Scheduling", "Doctor and nurse shift planning.", "pages/13_Staff_Scheduling.py"),
    ("⚙️", "Resource Allocation", "Ventilators, oxygen units and medical equipment tracking.", "pages/14_Resource_Allocation.py"),
    ("🧪", "Medical Report Analysis", "Detect abnormal lab values and generate risk alerts.", "pages/15_Medical_Report_Analysis.py"),
    ("🚨", "Emergency Alert", "Critical condition detection and emergency notifications.", "pages/16_Emergency_Alert.py"),
    ("💬", "AI Chatbot Assistant", "Healthcare FAQ, symptom guidance and appointment help.", "pages/17_AI_Chatbot_Assistant.py"),
    ("📊", "Analytics Dashboard", "Disease, bed, resource and recovery analytics.", "pages/18_Analytics_Dashboard.py"),
    ("🔔", "Notifications", "Appointment, medicine, report and emergency alerts.", "pages/19_Notifications.py"),
    ("📄", "Reporting Module", "Disease statistics, resource usage and recovery reports.", "pages/20_Reporting_Module.py"),
]

st.markdown("<div class='main-title'>🏥 AI-Powered Healthcare Prediction & Resource Management System</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Smart healthcare platform for disease prediction, patient care, hospital analytics and resource optimization</div>", unsafe_allow_html=True)

if not st.session_state.logged_in:
    c1, c2, c3 = st.columns([1, 1.2, 1])

    with c2:
        st.markdown("<div class='login-box'>", unsafe_allow_html=True)

        st.subheader("🔐 Login Portal")

        role = st.selectbox("Select Role", ["Patient", "Doctor", "Admin"])
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login", use_container_width=True):
            user = login_user(username, password, role)

            if user:
                st.session_state.logged_in = True
                st.session_state.role = role
                st.session_state.username = username
                st.success(f"Login successful as {role}")
                st.rerun()
            else:
                st.error("Invalid username, password, or role")

        st.info("Patient: patient / patient123 | Doctor: doctor / doctor123 | Admin: admin / admin123")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("📌 Project Modules Overview")

    cols = st.columns(4)
    for i, (icon, title, desc, link) in enumerate(modules):
        with cols[i % 4]:
            st.markdown(
                f"""
                <div class='module-card'>
                    <div class='module-title'>{icon} {title}</div>
                    <div class='module-desc'>{desc}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

else:
    st.sidebar.success(f"Logged in as {st.session_state.role}")
    st.sidebar.write(f"User: {st.session_state.username}")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.role = None
        st.session_state.username = None
        st.rerun()

    st.success(f"Welcome {st.session_state.role}! Choose a module below.")

    st.markdown("## 🚀 Module Navigation")

    cols = st.columns(4)
    for i, (icon, title, desc, link) in enumerate(modules):
        with cols[i % 4]:
            st.markdown(
                f"""
                <div class='module-card'>
                    <div class='module-title'>{icon} {title}</div>
                    <div class='module-desc'>{desc}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.page_link(link, label=f"Open {title}", icon=icon)