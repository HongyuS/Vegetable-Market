import random

START_BOARD = [[1,2,3],[4,5,6],[7,8,0]]
LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'

def print_board(board):                    # function to print the board
    print('')
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 0:
                print('  ', ' ', end='')
            else:
                print('  ', board[x][y], end='')
        print('\n')

def random_board(board):                   # function to generate a new puzzle
    list1 = [0,1,2,3,4,5,6,7,8]
    random.shuffle(list1)
    inversion = 0
    for i in range(len(list1)):
        for j in range(i, len(list1)):
            if list1[i] > list1[j] and\
                list1[i] != 0 and\
                list1[j] != 0:
                inversion += 1
    if inversion % 2 == 0:            # check solvability
        while list1 != []:
            board.append(list1[:3])
            list1 = list1[3:]
    else:
        random_board(board)

def operate(board, valid_direction, zero):   # function to move a number
    while True:
        direction = input('Input sliding direction (' + valid_direction + ') > ')
        if (direction == LEFT and zero[1] == 2)or\
            (direction == RIGHT and zero[1] == 0)or\
            (direction == UP and zero[0] == 2)or\
            (direction == DOWN and zero[0] == 0)or\
            not (direction in [LEFT, RIGHT, UP, DOWN]):
            print('Invalid move! Please try again!')
        else:
            if direction == LEFT:
                board[zero[0]][zero[1]] = board[zero[0]][zero[1]+1]
                board[zero[0]][zero[1]+1] = 0
            elif direction == RIGHT:
                board[zero[0]][zero[1]] = board[zero[0]][zero[1]-1]
                board[zero[0]][zero[1]-1] = 0
            elif direction == UP:
                board[zero[0]][zero[1]] = board[zero[0]+1][zero[1]]
                board[zero[0]+1][zero[1]] = 0
            elif direction == DOWN:
                board[zero[0]][zero[1]] = board[zero[0]-1][zero[1]]
                board[zero[0]-1][zero[1]] = 0
            print_board(board)
            break
    return board

def find_zero(board):                      # function to find where the zero is
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 0:
                zero = (x,y)
    return zero

def judge_direction(zero):            # function to judge valid direction
    direction_list = ['left', 'right', 'up', 'down']
    valid_direction = str()
    if zero[1] == 2:
        del direction_list[0]
    elif zero[1] == 0:
        del direction_list[1]
    if zero[0] == 2:
        del direction_list[-2]
    elif zero[0] == 0:
        del direction_list[-1]
    for i in range(len(direction_list)-1):
        valid_direction += direction_list[i] + ', '
    valid_direction += direction_list[len(direction_list)-1]
    return valid_direction

def new_game():                       # main game loop
    move = 0
    board = []
    random_board(board)
    print_board(board)
    while True:
        zero = find_zero(board)
        valid_direction = judge_direction(zero)
        board = operate(board, valid_direction, zero)
        move += 1
        if board == START_BOARD:
            print('Congratulations! You solved the puzzle in', move, 'moves!')
            break
    y_or_n = input('Do you want to start a new game (Y/N)? ')
    if y_or_n == 'Y' or y_or_n == 'y':
        new_game()

input('Welcome to 8-puzzle game, ………\nPress any key to begin >')
new_game()
