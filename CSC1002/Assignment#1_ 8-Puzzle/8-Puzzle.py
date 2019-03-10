import random

START_BOARD = [[1,2,3],[4,5,6],[7,8,0]]
LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'

def print_board(p_board):                           # function to print the board
    print('')
    for x in range(len(p_board)):
        for y in range(len(p_board[x])):
            if p_board[x][y] == 0:
                print('  ', ' ', end='')
            else:
                print('  ', p_board[x][y], end='')
        print('\n')

def random_board(p_board):                          # function to generate a new puzzle
    list1 = [0,1,2,3,4,5,6,7,8]
    random.shuffle(list1)
    inversion = 0
    for i in range(len(list1)):
        for j in range(i, len(list1)):
            if list1[i] > list1[j]\
                and list1[i] != 0\
                and list1[j] != 0:
                inversion += 1
    if inversion % 2 == 0:                          # check solvability
        while list1 != []:                          # if total_inversion is odd:
            p_board.append(list1[:3])               #     the puzzle is unsolvable
            list1 = list1[3:]                       # ///algorithm from internet///
    else:
        random_board(p_board)

def find_zero(p_board):                             # function to find where the zero is
    for x in range(len(p_board)):
        for y in range(len(p_board[x])):
            if p_board[x][y] == 0:
                zero = (x,y)
    return zero

def judge_direction(p_zero):                        # function to judge valid direction
    valid = 'left, right, up, down'
    if p_zero[1] == 2:                              # take out invalid item from the list
        valid = valid.replace('left, ','')
    elif p_zero[1] == 0:
        valid = valid.replace('right, ','')
    if p_zero[0] == 2:
        valid = valid.replace('up, ','')
    elif p_zero[0] == 0:
        valid = valid.replace(', down','')
    return valid

def operate(p_board, p_valid_direction, p_zero):    # function to move a number
    while True:
        direction = input('Input sliding direction (' + p_valid_direction + ') >')
        if (direction == LEFT and p_zero[1] == 2)or\
            (direction == RIGHT and p_zero[1] == 0)or\
            (direction == UP and p_zero[0] == 2)or\
            (direction == DOWN and p_zero[0] == 0)or\
            not (direction in [LEFT, RIGHT, UP, DOWN]):
            print('Invalid move! Please try again!')
        else:
            if direction == LEFT:
                p_board[p_zero[0]][p_zero[1]], p_board[p_zero[0]][p_zero[1]+1]\
                = p_board[p_zero[0]][p_zero[1]+1], 0
            elif direction == RIGHT:
                p_board[p_zero[0]][p_zero[1]], p_board[p_zero[0]][p_zero[1]-1]\
                = p_board[p_zero[0]][p_zero[1]-1], 0
            elif direction == UP:
                p_board[p_zero[0]][p_zero[1]], p_board[p_zero[0]+1][p_zero[1]]\
                = p_board[p_zero[0]+1][p_zero[1]], 0
            elif direction == DOWN:
                p_board[p_zero[0]][p_zero[1]], p_board[p_zero[0]-1][p_zero[1]]\
                = p_board[p_zero[0]-1][p_zero[1]], 0
            print_board(p_board)
            break

def new_game():                                     # main game loop
    move = 0
    board = []
    random_board(board)
    print_board(board)
    while True:
        zero = find_zero(board)
        valid_direction = judge_direction(zero)
        operate(board, valid_direction, zero)
        move += 1
        if board == START_BOARD:
            print('Congratulations! You solved the puzzle in', move, 'moves!')
            break
    y_or_n = input('Do you want to start a new game (Y/N)? ')
    if y_or_n == 'Y' or y_or_n == 'y':
        new_game()
    else:
        print('\nHave a nice day!\nSee you next time!')

input('Welcome to 8-puzzle game, ………\nPress any key to begin >')
new_game()
