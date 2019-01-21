while True:
    n = input("Which term to start with?\n>>>")
    if n.isdigit() and int(n) >= 0 and int(n) <= 1000000:
        n0 = n = int(n)
        break

n_thTerm = input("Please enter n-th term:\n>>>")
while True:
    try:
        float(eval(n_thTerm))
    except:
        print("Error!\nPlease check your formula, and enter again:")
        n_thTerm = input(">>>")
    else:
        break

nMax_end = [10, 100, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 1000000]

i = 0
while True:
    if n0 > nMax_end[i]:
        del nMax_end[i]
    else:
        break

_sum = 0

for nMax in nMax_end:
    while n <= nMax:
        _sum += eval(n_thTerm)
        n = n + 1
    print("\nThe sum from ", n0, " to ", n-1, "-th term is:\n", _sum, "\n", sep="")
    if nMax < 1000000:
        _continue = input("Enter to continue.\nType in anything else to stop the program.\n>>>")
        if bool(_continue) == True:
            print("Finished\n")
            break

feedback = input("Is your problem solved?\n>>>")
while feedback != "yes" and feedback != "no":
    print("Please enter \"yes\" or \"no\".\n", end="")
    feedback = input("Is your problem solved?\n>>>")
else:
    if feedback == "yes":
        print("Good luck!")
    else:
        print("Sorry to hear that!\nThere\'s nothing I can do.")

# e.g. (2*n + 1) / (n ** 2 * (n + 1) ** 2)
# e.g. 2 ** n * 3 ** n / n ** n
