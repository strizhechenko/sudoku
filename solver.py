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
        return int(x / 3) * 3, int(x / 3) * 3 + 3

    def block(self, x, y, m):
        subset = m[y[0]:y[1]]
        return [sub[x[0]:x[1]] for sub in subset]

    def solve(self):
        """
        Способ решения пока только один и самый простой по сути:
        1. Вычисляем какие цифры уже есть в блоке, ряду и колонке
        2. Все эти цифры вычитаем из списка возможных цифр
        3. Если останется 1 цифра - мы разгадали.
        TODO: добавить следующий способ
        1. В квадрате несколько пустых клеток с разными наборами потенциальных значений вычисленных способом 1
        2. Если какое-либо потенциальное значение встречается только в одной пустой клетке - значит мы разгадали
        TODO: добавить следующий способ
        1. Если в кубе нет цифры
        2. Если в первом соседнем кубе по одной линии (вертикально/горизонтально) она есть
        3. Если в втором соседнем кубе по одной линии эта цифра потенциально присутствует только в одной строке/колонке
        4. То в нашем кубе эта цифра находится на другой строке/колонке
        5. И если в этой строке/колонке уже разгаданы две цифры
        6. То искомая цифра находится именно там
        """
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
                    result = possible_values.pop()
                    print('[{0}, {1}] -> {2}'.format(x, y, result))
                    self.board[x][y] = result
                    return self.solve()
        return self.board
