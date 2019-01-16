weight = float(input("Please enter your weight(kg):\n>"))
height = float(input("Please enter your height(m):\n>"))

userBMI = weight / height ** 2
print("Your BMI (body max index) is ", userBMI, ".", sep="")

if userBMI < 24.0 and userBMI >= 18.5:
    print("Congratulations! You are very healthy!")
elif userBMI >= 24.0:
    print("You need to lose weight!")
else:
    print("Try to eat more fat!")
