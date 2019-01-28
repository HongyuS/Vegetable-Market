result = 0

while True:
    n = input("Please enter a number >")
    if n == "stop":
        break
    try:
        n = float(n)
    except:
        print("Invalid number. Please enter again.")
        continue
    result += n

print("The sum is " + str(result) + ".")
