# coding=utf-8
from solver import Board
from test_assets import board_hard, board_easy

if __name__ == '__main__':
    board = Board(board_easy)
    print(board)
    print()
    board.solve()
    print()
    print(board)
