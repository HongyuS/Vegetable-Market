nums=[]

def promptNumber1():
    n1=input('enter first number >')
    n1=int(n1)
    nums.append(n1)

def promptNumber2():
    n2=input('enter second number >')
    n2=int(n2)
    nums.append(n2)

def promptNumber3():
    n3=input('enter third number >')
    n3=int(n3)
    nums.append(n3)

def findMax():
    if nums[0] >= nums[1] and nums[0] >= nums[2]:
        print(nums[0])
    elif nums[1] >= nums[0] and nums[1] >= nums[2]:
        print(nums[1])
    else:
        print(nums[2])

promptNumber1()
promptNumber2()
promptNumber3()
findMax()
