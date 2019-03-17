def enterFloat(valueName):
    x = input("Enter the " + valueName + ": ")
    while True:
        try:
            float(eval(x))
        except:
            x = input("Error!\nPlease enter" + valueName + "again: ")
        else:
            break
    return float(x)

final = enterFloat("final account value")
rate = enterFloat("annual interest rate") / 100

while True:
    n = input("Enter the number of years: ")
    if n.isdigit():
        n = int(n)
        break
    else:
        print("Improper input! Try again.")

initial = final / (1 + rate) ** n
print("The initial value is:", initial)
