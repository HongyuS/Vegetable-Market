month, day = eval(input("month, day"))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    day += 1
    if day > 31:
        day = 1
        month += 1
        if month > 12:
            month = 1
elif month == 4 or month == 6 or month == 9 or month == 11:
    day += 1
    if day > 30:
        day = 1
        month += 1
else:
    day += 1
    if day > 28:
        day = 1
        month += 1

print(month, day)
