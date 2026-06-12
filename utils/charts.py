import pandas as pd
import plotly.express as px

def disease_distribution_chart():
    df = pd.DataFrame({
        "Disease": ["Diabetes", "Heart Disease", "Kidney Disease", "Hypertension", "Asthma"],
        "Cases": [420, 280, 150, 300, 100]
    })
    return px.bar(df, x="Disease", y="Cases", title="Disease Distribution")

def bed_occupancy_chart():
    df = pd.DataFrame({
        "Ward": ["General", "ICU", "Emergency", "Pediatric", "Maternity"],
        "Occupied": [50, 18, 12, 9, 6],
        "Available": [30, 7, 8, 6, 4]
    })
    return px.bar(df, x="Ward", y=["Occupied", "Available"], title="Bed Occupancy Analysis")

def appointment_status_chart():
    df = pd.DataFrame({
        "Status": ["Approved", "Pending", "Completed", "Rescheduled"],
        "Count": [25, 12, 10, 3]
    })
    return px.pie(df, values="Count", names="Status", title="Appointment Status")

def resource_utilization_chart():
    df = pd.DataFrame({
        "Resource": ["Ventilators", "Oxygen Units", "Monitors", "Wheelchairs", "ICU Beds"],
        "Utilization": [75, 83, 70, 60, 88]
    })
    return px.line(df, x="Resource", y="Utilization", markers=True, title="Resource Utilization Trend")

def staff_shift_chart():
    df = pd.DataFrame({
        "Shift": ["Morning", "Evening", "Night"],
        "Staff Count": [45, 38, 30]
    })
    return px.bar(df, x="Shift", y="Staff Count", title="Staff Shift Allocation")

def report_risk_chart():
    df = pd.DataFrame({
        "Risk Level": ["Low", "Medium", "High"],
        "Reports": [25, 15, 10]
    })
    return px.pie(df, values="Reports", names="Risk Level", title="Medical Report Risk Analysis")