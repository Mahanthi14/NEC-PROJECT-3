import pandas as pd

def get_beds():

    return pd.read_csv(
        "datasets/beds.csv"
    )