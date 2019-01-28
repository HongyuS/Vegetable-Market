# Working payment: for the part more than 40 hours, 1.5 times pay rate.

while True:
    time = input("Please enter your working hours:\n>>>")
    try:
        time = float(time)
    except:
        continue
    else:
        break

while True:
    rate = input("Please enter your salary per hour:\n>>>")
    try:
        rate = float(rate)
    except:
        continue
    else:
        break

if time > 40:
    salary = 40 * rate + 1.5 * rate * (time - 40)
else:
    salary = time * rate

print("Your salary is " + str(salary) + ".")
