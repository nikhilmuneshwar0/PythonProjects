height = int(input("What is your height in cm?\n"))

if height >= 120:
    print("You can ride the rollerCoster")
    age = int(input("What is your age?\n"))
    photo = input("Do you want a photo? yes/no")

    if age < 12:
        print("Your ticket price is $5.")
    elif age <= 18:
        print("Your ticket price is $7.")
    elif age >= 45 and age <= 50:
        print("Your tickets are free.")
    else:
        print("Your ticket price is $12.")

    if photo == "yes":
        print("Extra $3")
    else:
        print()

else:
    print("You cannot ride the rollerCoaster")
