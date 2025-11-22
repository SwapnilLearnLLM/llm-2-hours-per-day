height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = float(weight) / (float(height) ** 2)

print("Your BMI is " + str(bmi))

print(round(bmi, 2))