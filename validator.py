from itertools import product
from numpy import matrix


blocks = ((0, 3), (3, 6), (6, 9))
valid_digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def flat(m):
    return matrix(m).flatten().tolist()[0]


def validValues(board):
    return set(flat(board)) == valid_digits


def validRows(board):
    return all(validValues(row) for row in board)


def validColumns(board):
    return validRows(zip(*board))


def block(x, y, m):
    return [sub[x[0]:x[1]] for sub in m[y[0]:y[1]]]


def validBlocks(board):
    return all(validValues(flat(block(x, y, board))) for x, y in product(blocks, blocks))


def validSolution(board):
    return all(func(board) for func in (validValues, validRows, validColumns, validBlocks))
