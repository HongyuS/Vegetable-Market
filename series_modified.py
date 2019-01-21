n = int(input("Which term to start with?\n>>>"))
n0 = n
nMax_end = [10, 100, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 1000000]
n_thTerm = input("Please enter n-th term:\n>>>")
print("\n", end="")
_sum = 0

for nMax in nMax_end:
    while n <= nMax:
        _sum = _sum + eval(n_thTerm)
        n = n + 1
    print("The sum from ", n0, " to ", n-1, "-th term is:\n", _sum, "\n", sep="")

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
