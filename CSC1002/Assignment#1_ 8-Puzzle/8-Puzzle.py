import random

g_move = 0
g_board = []

START_BOARD = [[1,2,3],[4,5,6],[7,8,0]]
LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'

def print_board():                    # function to print the board
    global g_board
    print('')
    for x in range(len(g_board)):
        for y in range(len(g_board[x])):
            if g_board[x][y] == 0:
                print('  ', ' ', end='')
            else:
                print('  ', g_board[x][y], end='')
        print('\n')

def random_board():                   # function to generate a new puzzle
    global g_board
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
            g_board.append(list1[:3])
            list1 = list1[3:]
    else:
        random_board()

def move(direction, zero):            # function to move a number
    global g_board, g_move
    if (direction == LEFT and zero[1] == 2)or\
        (direction == RIGHT and zero[1] == 0)or\
        (direction == UP and zero[0] == 2)or\
        (direction == DOWN and zero[0] == 0)or\
        not (direction in [LEFT, RIGHT, UP, DOWN]):
        print('Invalid move! Please try again!')
    else:
        if direction == LEFT:
            g_board[zero[0]][zero[1]] = g_board[zero[0]][zero[1]+1]
            g_board[zero[0]][zero[1]+1] = 0
        elif direction == RIGHT:
            g_board[zero[0]][zero[1]] = g_board[zero[0]][zero[1]-1]
            g_board[zero[0]][zero[1]-1] = 0
        elif direction == UP:
            g_board[zero[0]][zero[1]] = g_board[zero[0]+1][zero[1]]
            g_board[zero[0]+1][zero[1]] = 0
        elif direction == DOWN:
            g_board[zero[0]][zero[1]] = g_board[zero[0]-1][zero[1]]
            g_board[zero[0]-1][zero[1]] = 0
        print_board()
        g_move += 1

def find_zero():                      # function to find where the zero is
    global g_board
    zero = None
    for x in range(len(g_board)):
        for y in range(len(g_board[x])):
            if g_board[x][y] == 0:
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

def ask_direction(valid_direction):   # function to input direction
    print('Input sliding direction (' + valid_direction + ') >', end = '')
    direction = input('')
    return direction

def judge_end_of_game():              # function to judge whether the puzzle is solved
    global g_board, g_move
    if g_board == START_BOARD:
        print('Congratulations! You solved the puzzle in', g_move, 'moves!')
        end = True
    else:
        end = False
    return end

def new_game():                       # main game loop
    global g_move
    random_board()
    print_board()
    while not judge_end_of_game():
        zero = find_zero()
        valid_direction = judge_direction(zero)
        direction = ask_direction(valid_direction)
        move(direction, zero)
    y_or_n = input('Do you want to start a new game (Y/N)? ')
    if y_or_n == 'Y' or y_or_n == 'y':
        g_move = 0
        new_game()

input('Welcome to 8-puzzle game, ………\nPress any key to begin >')
new_game()
