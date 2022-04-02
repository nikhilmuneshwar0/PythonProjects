height = float(input("enter your height in m: \n"))
weight = float(input("enter your weight in kg: \n"))

w1 = float(weight)
h1 = float(height)
bmi = w1/(h1**2)
bmi1 = float(bmi)
bmi2 = round(bmi1)

if bmi2 <= 18.5:
    print(f"Your BMI is {bmi2}, you are underweight.")
elif bmi2 >= 18.5 and bmi1 <= 25:
    print(f"Your BMI is {bmi2}, you have a normal weight.")
elif bmi2 >=25 and bmi2 < 30:
    print(f"Your BMI is {bmi2}, you are slightly overweight.")
elif bmi2 >30 and bmi2 < 35:
    print(f"Your BMI is {bmi2}, you are obese.")
else:
    print(f"Your BMI is {bmi2}, you are clinically obese.")
