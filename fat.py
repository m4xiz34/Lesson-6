height = float(input("Enter your height here:   "))
weight = float (input("Enter your weight here:  "))

BMI = weight / (height/100)**2

if BMI <= 18.4:
    print("You are underweight")
elif BMI <= 24.9:
    print("You are healthy")
elif BMI <= 29.9:
    print("You are overweight")
elif BMI <= 34.8:
    print("You are severely overweight")
else:
    print("You are obese")
