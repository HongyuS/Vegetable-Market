# variables
nums=[]

def promptNumber(desc):
    while True:
        n1=input('enter ' + desc + ' number >')
        if n1.isdigit():
            n1=int(n1)
            nums.append(n1)
            break
        
def findMax():
    m = findLarger(nums[0],nums[1])
    m = findLarger(m,nums[2])
    print(m)

def findLarger(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

promptNumber('first')
promptNumber('second')
promptNumber('third')
findMax()