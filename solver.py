# coding: utf-8
from operator import add
from functools import reduce

VALID_DIGITS = {1, 2, 3, 4, 5, 6, 7, 8, 9}


class Node(object):
    """ Одна точка на поле """
    possible_values = []

    def __init__(self, value):
        self.value = value


class Board(object):
    """ Поле sudoku """

    def __init__(self, board):
        self.board = board

    def __str__(self):
        return "\n".join(" ".join(str(col) for col in row) for row in self.board)

    def block_range(self, x):
        return int(x / 3 * 3), int(x / 3 * 3 + 3)

    def block(self, x, y, m):
        subset = m[y[0]:y[1]]
        return [sub[x[0]:x[1]] for sub in subset]

    def solve(self):
        for x in range(9):
            for y in range(9):
                if self.board[x][y] != 0:
                    continue
                row = set(self.board[x])
                inverted = list(zip(*self.board))[y]
                column = set(inverted)
                sub_block = self.block(self.block_range(y), self.block_range(x), self.board)
                block3x3 = set(reduce(add, sub_block))
                possible_values = VALID_DIGITS - (row | column | block3x3)
                if len(possible_values) == 1:
                    self.board[x][y] = possible_values.pop()
                    return self.solve()
        return self.board
