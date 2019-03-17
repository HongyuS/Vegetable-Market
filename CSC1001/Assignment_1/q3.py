n = 0
while True:
    m = (input("Enter a number: "))
    try:
        m = float(m)
    except:
        pass
    else:
        break

while n ** 2 < m:
    n += 1

print(n)
