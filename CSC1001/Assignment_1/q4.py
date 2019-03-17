while True:
    n = input('Enter a number N: ')
    try:
        n = int(n)
    except:
        pass
    else:
        if n > 0:
            break
    print('Please input a positive INTEGER')

print('\nm\tm+1\tm**(m+1)')
for i in range(n):
    m = i + 1
    print(m, '\t', m + 1, '\t', m ** (m + 1), sep='')
print('\nFinished\n')
