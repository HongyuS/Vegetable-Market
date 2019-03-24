'''
This program can only generate 8 different solutions for 8-Queen Puzzle
'''

from random import randint 

BOARD_DIM = 8

def printBoard(solution, dim=BOARD_DIM):
    s = tuple(solution)
    for x in range(dim):                              # print one row
        print('|', end='')
        for y in range(dim):
            if s[x][1] == y:
                print('Q|', end='')
            else:
                print(' |', end='')
        print()                                       # start a new row

def solveQueens(dim=BOARD_DIM):
    solution = [randint(0, 7)]                        # generate a random position for the 1st row
    col = 0
    while True:
        row = len(solution)                           # go to the next row
        while col < dim and not\
                all(
                    y != col                          # not in the same column
                    and abs(x - row) != abs(y - col)  # not in the same diagonal
                    for x, y in enumerate(solution)   # check every position before
                ):
            col += 1                                  # go to the next column
        if col < dim:
            solution.append(col)                      # add one valid position to the list
            if row == dim - 1:
                return enumerate(solution)            # return all queens' position
            else:
                col = 0
        else:
            col = solution.pop() + 1                  # go to the next position of the last row

if __name__ == '__main__':
    printBoard(solveQueens())
