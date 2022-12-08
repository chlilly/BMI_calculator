height = input("Enter your height in inches: ")
weight = input("Enter your weight in lb: ")

bmi = int(weight) / float(height) ** 2

bmi_as_int = int(bmi)
print(bmi_as_int)
