height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = weight / (height**2)
bmi_decimal = round(bmi, 2)
bmi_final = round(bmi)
perfect_weight = 25 * (height**2)
perfect = round(perfect_weight, 2)
if bmi_decimal <= 18.5:
    print(f"Your BMI is {bmi_final}, you are underweight.")
    print(f"For a perfect BMI, your weight must be {perfect}")
elif bmi_decimal <= 25:
    print(f"Your BMI is {bmi_final}, you have a normal weight.")
    print("please maintain the same weight for a healthy body")
elif bmi_decimal <= 30:
    print(f"Your BMI is {bmi_final}, you are slightly overweight.")
    print(f"For a perfect BMI, your weight must be {perfect}")
elif bmi_decimal <= 35:
    print(f"Your BMI is {bmi_final}, you are obese.")
    print(f"For a perfect BMI, your weight must be {perfect}")
else:
    print(f"Your BMI is {bmi_final}, you are clinically obese.")
    print(f"For a perfect BMI, your weight must be {perfect}")

