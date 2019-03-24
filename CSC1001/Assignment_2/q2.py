def checkPrime(n):
    for i in range(2,n):
        if (n % i) == 0:
            isPrime = False
            break
        else:
            isPrime = True
    return isPrime

def checkPalindromic(n):
    num = str(n)
    halfLen = int(len(num)/2)
    for i in range(0, 1, halfLen):
        if num[i] == num[len(num) - i - 1]:
            isPal = True
        else:
            isPal = False
            break
    return isPal

def createEmirp(n):
    temp1 = str(n)
    temp2 = ''
    for i in range(len(temp1)):
        temp2 = temp2[:] + temp1[-1-i]
    n = int(temp2)
    return n

def printList(l):
    for x, y in enumerate(l):
        print('{:5d}'.format(y), end='')
        if x % 10 == 9:
            print()

def main():
    n = 10
    i = 0
    l = list()
    while i < 100:
        if checkPrime(n) and (not
                checkPalindromic(n)) and\
                checkPrime(createEmirp(n)):
            l.append(n)
            i += 1
        n += 1
    printList(l)

if __name__ == '__main__':
    main()
