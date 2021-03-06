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

# augmented assignment
x1 = 22
x1 += 7
x1 -= 2 * 7
print(x1)
print("End of example #8\n")

# Data type
a1 = 100 + 200           # int
a2 = "100" + "200"       # string
print(a1, a2)
type(a1)                 # check data type
a1 += 1.23               # float
type(a1)

# the type can be changed
y1 = "hello"
y2 = 34
type(y1), type(y2)
y1 = y2 + 23
y2 += 1.2
type(y1), type(y2)

# Type conversions
a1 = 100
type(a1)
a1 = float(a1)
type(a1)
a1 = "100"
a1 = int(a1)
a1 += a1
type(a1)
print(a1)
a1 = str(a1)
type(a1)
print("End of example #9\n")

# User input
a3 = input()
a4 = input()
print(type(a3), type(a4))     # the input func always inputs strings
print(a3 + a4)
a5 = int(input())
print(type(a5))
print("End of example #10\n")

# String operations
# "+": concatenation
# "*": multiple concatenation
a6 = "thieIsAString\n"
a7 = "hahaha\n"
a6 = a6 + a7
a6 += a7
print(a6)
a7 = a7 * 3
print(a7)
print("End of example #11\n")

# eval()
# input a str, take it as a py expression
_str = "34 + 7 * 4"
print(_str)
_int = eval(_str)
print(_int)
eval("print(\"Hello, world!\")")

# x, y = float(input("please enter \"23, 34\"\n>>>"))
# print(x, y)
# why error?
a, b = eval(input("please enter \"23, 34\"\n>>>"))
print(a, b)
print("End of example #12\n")
