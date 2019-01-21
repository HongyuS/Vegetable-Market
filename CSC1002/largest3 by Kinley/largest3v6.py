nums=[]

def promptNumber(desc):
    while True:
        n1=input('enter ' + desc + ' number >')
        if n1.isdigit():
            nums.append(int(n1))
            break

def findMax():
    print('largest number:',max(nums))

promptNumber('first')
promptNumber('second')
promptNumber('third')
findMax()

