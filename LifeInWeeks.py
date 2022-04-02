#Tell your remaining time of your life if you live upto 90 years old.
age = input("What is your current age?")

newAge = int(age)
RTime = 90 - newAge
days = RTime * 365
weeks = RTime * 52
months = RTime * 12
print(f"You have {days} days, {weeks} weeks, and {months} months left.")



