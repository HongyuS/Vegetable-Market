'''
L1 will be changed by S1
L2 will be changed by S1 & S2
L3 will be changed by S1 & S3
…………
L25 will be changed by S1, S5, S25
…………
L34 will be changed by S1, S2, S17, S34
…………
It is easy to know that:
the code of student who changes the locker
equals to the locker number's factors.
So, the lockers with odd number of factors
will stay open.
'''

def findFactor(num):    # find all factors
    n = 1
    l = list()
    while n <= num:
        if num % n == 0:
            l.append(n)
        n += 1
    return l

def isOpen(num):        # check odd/even
    x = len(findFactor(num))
    if x % 2 == 1:
        return True
    else:
        return False

def main():
    num = 1
    label = str()
    while num <= 100:
        if isOpen(num):
            label = label + ' L' + str(num)
        num += 1
    print('The open lockers are:' + label)

if __name__ == "__main__":
    main()
