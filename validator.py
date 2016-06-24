from operator import add
from numpy import matrix

wrong_sudoku = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 0, 3, 4, 9],
                [1, 0, 0, 3, 4, 2, 5, 6, 0],
                [8, 5, 9, 7, 6, 1, 0, 2, 0],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 0, 1, 5, 3, 7, 2, 1, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 0, 0, 4, 8, 1, 1, 7, 9]]

good_sudoku = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
               [6, 7, 2, 1, 9, 5, 3, 4, 8],
               [1, 9, 8, 3, 4, 2, 5, 6, 7],
               [8, 5, 9, 7, 6, 1, 4, 2, 3],
               [4, 2, 6, 8, 5, 3, 7, 9, 1],
               [7, 1, 3, 9, 2, 4, 8, 5, 6],
               [9, 6, 1, 5, 3, 7, 2, 8, 4],
               [2, 8, 7, 4, 1, 9, 6, 3, 5],
               [3, 4, 5, 2, 8, 6, 1, 7, 9]]


blocks = ((0, 3), (3, 6), (6, 9))
valid_digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def flatx(m):
    return matrix(m).flatten().tolist()[0]


def flat(m):
    return reduce(add, m)


def validValues(board):
    return set(flat(board)) == valid_digits


def validRows(board):
    return all(set(row) == valid_digits for row in board)


def validColumns(board):
    return validRows(zip(*board))


def flatblock(x, y, m):
    return flat([sub[x[0]:x[1]] for sub in m[y[0]:y[1]]])


def validBlocks(board):
    return all(all(validValues(flatblock(x, y, board)) for y in blocks) for x in blocks)


def validSolution(board):
    return all(func(board) for func in (validValues, validRows, validColumns, validBlocks))
