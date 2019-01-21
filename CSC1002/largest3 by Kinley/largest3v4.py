nums=[]

def promptNumber(desc):
    prompt='enter ' + desc + ' number >'
    n=input(prompt)
    n=int(n)
    nums.append(n)

def findMax():
    if nums[0] >= nums[1] and nums[0] >= nums[2]:
        print(nums[0])
    elif nums[1] >= nums[0] and nums[1] >= nums[2]:
        print(nums[1])
    else:
        print(nums[2])

promptNumber('first')
promptNumber('second')
promptNumber('third')
findMax()
