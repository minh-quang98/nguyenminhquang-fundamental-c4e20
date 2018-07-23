heic = int(input("Enter your height(cm): "))
wei = int(input("Enter your weight(kg): "))
heim = heic / 100
bmi = wei / (heim ** 2)
if bmi < 16:
    print("You are severely underweight")
elif bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You are normal")
elif bmi < 30:
    print("You are overweight")
else:
    print("You are obese")