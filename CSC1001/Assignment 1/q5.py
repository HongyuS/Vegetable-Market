while True:
    n = input('Enter an integer N: ')
    try:
        n = int(n)
    except:
        pass
    else:
        if n > 1:
            break
    print('Please input an INTEGER larger than one!')

l = []
for num in range(n):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            l.append(num)

print('The prime numbers smaller than', n, 'include:')
for x, y in enumerate(l):
    print(y, end=' ')
    if x % 8 == 7:
        print()
print()
