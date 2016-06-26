from operator import add

valid_digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def _range(x):
    return x / 3 * 3, x / 3 * 3 + 3


def block(x, y, m):
    return [sub[x[0]:x[1]] for sub in m[y[0]:y[1]]]

def solve(board):
    for x in xrange(9):
        for y in xrange(9):
            if board[x][y] == 0:
                blk = set(reduce(add, block(_range(y), _range(x), board)))
                row = set(board[x])
                col = set(zip(*board)[y])
                possible_values = valid_digits - (blk | col | row)
                if len(possible_values) == 1:
                    board[x][y] = possible_values.pop()
                    return solve(board)
    return board