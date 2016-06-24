from operator import add
from numpy import matrix


blocks = ((0, 3), (3, 6), (6, 9))
valid_digits = set(xrange(1, 10))


def flat(m):
    return matrix(m).flatten().tolist()[0]


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
