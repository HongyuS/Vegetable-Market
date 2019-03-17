import random
piece=()
move = 0
empty_space=()
list1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#to get shuffled list
random.shuffle(list1)
print('\n'*2)
#to make list of lists
matrix=[]
while list1 !=[]:
    matrix.append(list1[:4])
    list1 = list1[4:]
# to find the empty space
# we can also delete this section and just add a one line
# empty_space = (x,y) before the print('|xx ..  ) statement
for x in range (len(matrix)):
    for y in range(len(matrix[x])):
        if matrix[x][y] == 0:
            empty_space = (x,y)
print()
#to print the list in two digit matrix 
while True:
    print('\n+----+----+----+---|')
    for x in range (len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == 0:
                print('|XX' , end='  ')
            else:
                 print('|' + '{:02d}' .format(matrix[x][y]), end='  ') 
        print('\n+----+----+----+---|')       
    #ask for the next move
    num = input('\nplease type the number of the piece to move : ( q ) to quit  ')
    if num in ['q','Q']:
        break
    num = int(num)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if num == matrix[i][j]:
                piece = (i,j)
    if num > 15:
        print('illegal move  ')
    else:
        if(empty_space==(piece[0]-1,piece[1]))\
           or(empty_space==(piece[0]+1,piece[1]))\
           or(empty_space==(piece[0],piece[1]-1))\
           or(empty_space==(piece[0],piece[1]+1)):
            matrix[empty_space[0]][empty_space[1]]=num
            matrix[piece[0]][piece[1]]=0
            empty_space=(piece[0],piece[1])
            move = move +1
            print()
            print('you have made ',move , 'moves so far ')
            print(2*'\n')
        else:
            print('illegal move , try again ')
print('game over  ')