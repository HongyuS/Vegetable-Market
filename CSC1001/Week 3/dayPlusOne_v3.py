# Add a day to a given date.

m, d = eval(input("month, day"))

dayOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while d > dayOfMonth[m - 1] or m >12 or d <= 0 or m <= 0:
    print("Invaliad date!")
    m, d = eval(input("month, day"))

d += 1

if d > dayOfMonth[m - 1]:
    d = 1
    m = m % 12 + 1

print(m, d)
