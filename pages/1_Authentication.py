import streamlit as st

st.set_page_config(
    page_title="Authentication",
    page_icon="🔐",
    layout="wide"
)

st.markdown("""
<style>
.main-title {
    font-size: 38px;
    font-weight: 800;
    color: #0f766e;
    text-align: center;
    margin-bottom: 5px;
}
.sub-title {
    font-size: 17px;
    color: #475569;
    text-align: center;
    margin-bottom: 30px;
}
.login-card {
    background: linear-gradient(135deg, #ecfeff, #f8fafc);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0px 6px 25px rgba(0,0,0,0.10);
}
.info-card {
    background: white;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🔐 Authentication & User Management</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Secure login system for Patient, Doctor, Admin, and Hospital Staff</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1.4, 1])

with col2:
    st.markdown("<div class='login-card'>", unsafe_allow_html=True)

    st.subheader("Login Portal")

    role = st.selectbox(
        "Select Role",
        ["Patient", "Doctor", "Admin", "Hospital Staff"]
    )

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login", use_container_width=True):
        if role == "Patient" and username == "patient" and password == "patient123":
            st.success("Patient login successful")
            st.session_state["role"] = "Patient"

        elif role == "Doctor" and username == "doctor" and password == "doctor123":
            st.success("Doctor login successful")
            st.session_state["role"] = "Doctor"

        elif role == "Admin" and username == "admin" and password == "admin123":
            st.success("Admin login successful")
            st.session_state["role"] = "Admin"

        elif role == "Hospital Staff" and username == "staff" and password == "staff123":
            st.success("Hospital Staff login successful")
            st.session_state["role"] = "Hospital Staff"

        else:
            st.error("Invalid username or password")

    st.info("""
    Demo Login Details:

    Patient → patient / patient123  
    Doctor → doctor / doctor123  
    Admin → admin / admin123  
    Staff → staff / staff123
    """)

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("<div class='info-card'>👤<br><b>Patient Login</b><br>Health records & appointments</div>", unsafe_allow_html=True)

with c2:
    st.markdown("<div class='info-card'>🩺<br><b>Doctor Login</b><br>Patients & treatment plans</div>", unsafe_allow_html=True)

with c3:
    st.markdown("<div class='info-card'>🏥<br><b>Admin Login</b><br>Resources & analytics</div>", unsafe_allow_html=True)

with c4:
    st.markdown("<div class='info-card'>👨‍⚕️<br><b>Staff Login</b><br>Emergency & support tasks</div>", unsafe_allow_html=True)