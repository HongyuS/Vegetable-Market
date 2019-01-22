# 此程序检查输入的字符串是否对称
'''
• Ask the user for a string . Print out whether it is a
palindrome or not. (A palindrome is a string that reads the
same forwards and backwards.)
• Note: Python has its built-in reserve function, but DO NOT
USE IT FOR NOW!
'''

while True:
    _str = input("Enter anything:\n>>>")
    _len = len(_str)
    if _len > 1:
        break
    else:
        print("It is too short to be a palindrome.\nPlease try again.\n")

num = int(_len / 2)

for i in range(0,1,num):
    if _str[i] == _str[_len - i - 1]:
        print("It is a palindrome.\n")
    else:
        print("It is not a palindrome.\n")

print("Have fun!\n")
