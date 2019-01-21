n1=input('enter first number >')
n2=input('enter second number >')
n3=input('enter third number >')

n1=int(n1)
n2=int(n2)
n3=int(n3)

if n1 >= n2 and n1 >= n3:
    print(n1)
elif n2 >= n3:
    print(n2)
else:
    print(n3)
