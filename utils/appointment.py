import pandas as pd

def get_appointments():

    return pd.read_csv(
        "datasets/appointments.csv"
    )