def BMI(a, b):
    return a / (b ** 2)


x = int(input("Enter your weight in kilograms"))
y = float(input("Enter your height in metres"))
print(BMI(x, y))
