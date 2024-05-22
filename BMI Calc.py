print("Salut! et l'eau")
name = input("What is your name?")

weight = int(input("Enter your weight in pounds: "))

height = int(input("Enter your height in inches: "))

BMI = (weight * 703) / (height * height)

print(BMI)

if BMI > 0:
    if BMI < 18.5:
        print(name +", you are underweight.")
    elif BMI <= 24.9:
        print(name +", you're weight is cool.")
    elif BMI > 29.9:
        print(name +", you are overweigth.")
    else:
        print("You need to hit the gym")
else:         
    print("Enter valid Input")