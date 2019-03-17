while True:
    n = input("Enter an integer: ")
    if n.isdigit():
        length = len(n)
        break
    else:
        print("Improper input!")

for i in range(0,length):
    print(n[i])
