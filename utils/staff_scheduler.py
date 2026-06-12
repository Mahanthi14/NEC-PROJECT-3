def suggest_staff(patient_load):

    doctors = max(5, patient_load // 25)

    nurses = max(10, patient_load // 12)

    return doctors, nurses