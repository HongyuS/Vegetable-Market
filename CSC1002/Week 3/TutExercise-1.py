'''
• Create a program that asks users to enter their names and
ages. Print out a message that tells them the year when
they turn 100 years old.
• Ask the user for a number of times that they wish to repeat
that message. Then print out that many copies of the
previous message.
• Print out every message on a new line. (Hint: the string "\n”
is the same as pressing the ENTER button)
'''

name = input("Please enter your name: 😂\n>>>")
while True:
    age = input("Please enter your age:\n>>>")
    if age.isdigit():
        age = int(age)
        break

while True:
    i = input("Enter a natural number as \"repeat time\":\n>>>")
    if i.isdigit():
        i = int(i)
        break

year = 2019 - age + 100
message = "You will be 100 years old in year " + str(year) + ".\n"

while True:
    try:
        message * i
    except:
        while True:
                i = input("Enter a natural number as \"repeat time\":\n>>>")
                if i.isdigit():
                    i = int(i)
                    break
    else:
        break

print(message * i)
print("Have fun!\n")
