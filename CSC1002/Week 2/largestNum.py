# input 3 numbers & find the largest one without using "max()"

n1 = int(input('Please enter 3 numbers:\n>'))
n2 = int(input('>'))
n3 = int(input('>'))

if n1>=n2 and n1>=n3:
    print("\nThe largest number is", n1)
elif n2>=n1 and n2>=n3:
    print("\nThe largest number is", n2)
else:
    print("\nThe largest number is", n3)
