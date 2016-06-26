from operator import add

valid_digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def block_range(x):
    return x / 3 * 3, x / 3 * 3 + 3


def block(x, y, m):
    return [sub[x[0]:x[1]] for sub in m[y[0]:y[1]]]

def solve(board):
    for x in xrange(9):
        for y in xrange(9):
            if board[x][y] == 0:
                row = set(board[x])
                column = set(zip(*board)[y])
                block3x3 = set(reduce(add, block(block_range(y), block_range(x), board)))
                possible_values = valid_digits - (row | column | block3x3)
                if len(possible_values) == 1:
                    board[x][y] = possible_values.pop()
                    return solve(board)
    return board
