from numpy import matrix

valid_digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
blocks = [[1] * 3, [0] * 3 + [1] * 3, [0] * 6 + [1] * 3]


def validRows(board):
    return all(set(row) == valid_digits for row in board)


def validColumns(board):
    return validRows(zip(*board))


def validBlocks(board):
    flatblock = lambda x, y: matrix(board).compress(x, 0).compress(y, 1).flatten().tolist()[0]
    return all(all(set(flatblock(x, y)) == valid_digits for y in blocks) for x in blocks)


def validValues(board):
    return set(matrix(board).flatten().tolist()[0]) == valid_digits


def validSolution(board):
    return all(func(board) for func in (validValues, validRows, validColumns, validBlocks))
