n = int(input("PLease enter an integer:\n"))
nMax = int(input("PLease enter a larger integer:\n"))
n_thTerm = input("Please enter n-th term:\n")
_sum = 0

while n <= nMax:
    _sum = _sum + eval(n_thTerm)
    n = n + 1

print(_sum)
