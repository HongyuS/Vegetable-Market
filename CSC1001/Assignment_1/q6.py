from math import sin
from math import cos
from math import tan

def enterFloat(valueName):
    x = input("Enter end point" + valueName + ": ")
    while True:
        try:
            float(eval(x))
        except:
            x = input("Error!\nPlease enter" + valueName + "again: ")
        else:
            break
    return float(x)

while True:
    f = input('Please input the function type (sin, cos, tan): ')
    if f == 'sin' or f == 'cos' or f == 'tan':
        break
    else:
        print('Invalid function name!\nPlease try again!')

a = enterFloat('\"a\"')

while True:
    b = enterFloat('\"b\"')
    if b > a:
        break
    else:
        print('Please input a number larger than \"a\"!')

while True:
    n = input('Enter the number of sub-intervals: ')
    try:
        n = int(n)
    except:
        pass
    else:
        if n > 0:
            break
    print('Please input a positive INTEGER!')

n_sum = 0
if f == 'sin':
    for i in range(n):
        n_sum += (b-a)/n * sin(a + (b-a)/n * (i + 0.5))
elif f == 'cos':
    for i in range(n):
        n_sum += (b-a)/n * cos(a + (b-a)/n * (i + 0.5))
else:
    for i in range(n):
        n_sum += (b-a)/n * tan(a + (b-a)/n * (i + 0.5))
print('\nThe numerical integration of ' + f + '(x) over interval [' + str(a) + ', ' + str(b) + '] is:\n', n_sum, '\n', sep='')
