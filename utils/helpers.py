def calculate_bmi(
        weight,
        height):

    height = height / 100

    bmi = weight / (height ** 2)

    return round(bmi, 2)