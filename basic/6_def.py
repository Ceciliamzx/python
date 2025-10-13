# def
print("========== def ==========")
def colculate_BMI(height, weight):
    bmi = weight / (height * height)
    if bmi < 18.5:
        category = "underweight"
    elif 18.5 <= bmi < 24:
        category = "normal weight"
    elif 24 <= bmi < 28:
        category = "overweight"
    else:
        category = "obesity"
    print(f"您的bmi值为: {bmi:.2f}", f"您当前的体重状态为: {category}")
    return bmi
colculate_BMI(1.75, 70)