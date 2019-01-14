# conditional flow
x = 5
if x>20:
    print("bigger")
if x<10:
    print("smaller")
print("End of example #1\n")

# repeated flow
while x<10:
    print("菜市场")
    x = x+1
print("End of example #2\n")

# Cascaded assignment
y = z = x
print(x, y, z)
print("End of example #3\n")

a, b = 12, 20 # Simultaneous assignment
b, a = a, b
print(a, b)
print("End of example #4-1\n")

# exchange the values of two variables without using simultaneous assignment
p = 'Tom'
q = 'Luo'
print(p, q)
n = p
p = q
q = n
print(p, q)
print("End of example #4-2\n")

# test operator precedence rules
#     Highest to lowest precedence rule
# 􏰀        Parenthesis are always with highest priority 􏰀 Power
#         􏰀Multiplication, division and remainder 􏰀Addition and subtraction
# 􏰀        Left to right
x = 1+2**3/4*5
print(x)
print("End of example #5\n")

# Floor division
time1 = int(input("Please enter time (unit: s)"))
minutes = time1 // 60 # Number of complete minutes in time.
print("There are", minutes, "complete minutes in", time1, "seconds.")
print("End of example #6\n")

# divmod()
time2 = int(input("Please enter time (unit: s)"))
secPerMin = 60
_min, sec = divmod(time2, secPerMin)
print(_min, ":", sec, sep="")
print("End of example #7\n")
