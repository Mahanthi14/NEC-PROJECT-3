import pandas as pd
import random

diabetes_rows = []
for i in range(100):
    outcome = 1 if i % 2 == 0 else 0

    if outcome == 1:
        row = [
            random.randint(2, 10),
            random.randint(145, 210),
            random.randint(75, 110),
            random.randint(25, 45),
            random.randint(120, 260),
            round(random.uniform(31, 45), 1),
            round(random.uniform(0.45, 1.8), 3),
            random.randint(40, 70),
            1
        ]
    else:
        row = [
            random.randint(0, 4),
            random.randint(75, 125),
            random.randint(60, 85),
            random.randint(15, 30),
            random.randint(40, 130),
            round(random.uniform(19, 29), 1),
            round(random.uniform(0.10, 0.55), 3),
            random.randint(20, 40),
            0
        ]

    diabetes_rows.append(row)

diabetes_cols = [
    "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
    "Insulin", "BMI", "DiabetesPedigreeFunction", "Age", "Outcome"
]

pd.DataFrame(diabetes_rows, columns=diabetes_cols).to_csv(
    "datasets/diabetes.csv",
    index=False
)

heart_rows = []
for i in range(100):
    target = 1 if i % 2 == 0 else 0

    if target == 1:
        row = [
            random.randint(52, 75),
            random.randint(0, 1),
            random.choice([0, 2]),
            random.randint(140, 180),
            random.randint(240, 340),
            random.randint(0, 1),
            random.randint(0, 2),
            random.randint(95, 145),
            1,
            round(random.uniform(1.5, 4.0), 1),
            random.randint(0, 1),
            random.randint(1, 3),
            random.randint(2, 3),
            1
        ]
    else:
        row = [
            random.randint(30, 55),
            random.randint(0, 1),
            random.choice([1, 2, 3]),
            random.randint(100, 135),
            random.randint(150, 230),
            0,
            random.randint(0, 1),
            random.randint(150, 190),
            0,
            round(random.uniform(0.0, 1.2), 1),
            random.randint(1, 2),
            0,
            random.randint(1, 2),
            0
        ]

    heart_rows.append(row)

heart_cols = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target"
]

pd.DataFrame(heart_rows, columns=heart_cols).to_csv(
    "datasets/heart.csv",
    index=False
)

print("100 diabetes records created")
print("100 heart records created")