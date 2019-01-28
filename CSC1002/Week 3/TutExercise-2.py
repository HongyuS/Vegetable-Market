'''
• Ask the user for a number. Print out a message to tell the
user whether the number is even or odd. (Hint: how does
an even / odd number react differently when divided by 2?)
• If the number is a multiple of 4, print a different message.
• Ask the user for two numbers: one is the numerator (call it
num) and the other is the denominator (call it check). If
check divides evenly into num, tell the user; if not, print a
different message.
'''

def newLevel(title):
    print("\n>>> LEVEL " + title + " <<<\n")

def judge(_num, _check):
    return bool(_num % _check)

newLevel("ONE")

while True:
    n = input("Please enter an integer:\n>>>")
    if n.isdigit():
        n = int(n)
        break

if judge(n, 2):
    print("It is an odd number.\n")
else:
    if not judge(n, 4):
        print("It can be divided by 4.\n")
    else:
        print("It is an even number.\n")

newLevel("TWO")

while True:
    num = input("Please enter an integer as \"num\":\n>>>")
    check = input("Please enter another integer as \"check\":\n>>>")
    if num.isdigit() and check.isdigit():
        num = int(num)
        check = int(check)
        break

if not judge(num, check):
    print("The check divides evenly into num.\n")
else:
    print("The check can not divide evenly into num.\n")

print("Have fun!\n")
