m, d = eval(input("month, day"))

dayOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

d += 1

if d > dayOfMonth[m - 1]:
    d = 1
    m = m % 12 + 1

print(m, d)
