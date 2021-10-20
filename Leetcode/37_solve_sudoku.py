# QUESTION:
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all of the following rules:
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.
# Modify the board in-place

from typing import List
from pprint import pprint
from copy import deepcopy

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        possible_inputs = [[set() for _ in range(9)] for _ in range(9)]
        for y in range(9):
            for x in range(9):
                if board[y][x] == '.':
                    possible_inputs[y][x] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
                    for i in range(9):
                        if board[y][i] in possible_inputs[y][x]:
                            possible_inputs[y][x].remove(board[y][i])
                        if board[i][x] in possible_inputs[y][x]:
                            possible_inputs[y][x].remove(board[i][x])
                    for y_square in range(y // 3 * 3, y // 3 * 3 + 3):
                        for x_square in range(x // 3 * 3, x // 3 * 3 + 3):
                            if board[y_square][x_square] in possible_inputs[y][x]:
                                possible_inputs[y][x].remove(board[y_square][x_square])

        def next_index(y, x):
            if x < 8:
                return y, x + 1
            return y + 1, 0

        def solveSudokuHelp(board, y, x, possible_inputs):
            if y > 8:
                return board
            if board[y][x] != '.':
                return solveSudokuHelp(board, *next_index(y, x), possible_inputs)
            if not possible_inputs[y][x]:
                return False
            for possible_input in possible_inputs[y][x]:
                board[y][x] = possible_input
                new_possible_inputs = deepcopy(possible_inputs)
                for i in range(9):
                    if possible_input in new_possible_inputs[y][i]:
                        new_possible_inputs[y][i].remove(possible_input)
                    if possible_input in new_possible_inputs[i][x]:
                        new_possible_inputs[i][x].remove(possible_input)
                for y_square in range(y // 3 * 3, y // 3 * 3+ 3):
                    for x_square in range(x // 3 * 3, x // 3 * 3+ 3):
                        if possible_input in new_possible_inputs[y_square][x_square]:
                            new_possible_inputs[y_square][x_square].remove(possible_input)
                if solveSudokuHelp(board, *next_index(y, x), new_possible_inputs):
                    return board
                else:
                    board[y][x] = '.'
            return False

        solveSudokuHelp(board, 0, 0, possible_inputs)
        pprint(board)

# IDEA:
# backtracking

soln = Solution()
sample_sudoku = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
soln.solveSudoku(sample_sudoku)
sample_sudoku_2 = [
    [".",".","9","7","4","8",".",".","."],
    ["7",".",".",".",".",".",".",".","."],
    [".","2",".","1",".","9",".",".","."],
    [".",".","7",".",".",".","2","4","."],
    [".","6","4",".","1",".","5","9","."],
    [".","9","8",".",".",".","3",".","."],
    [".",".",".","8",".","3",".","2","."],
    [".",".",".",".",".",".",".",".","6"],
    [".",".",".","2","7","5","9",".","."]
]
soln.solveSudoku(sample_sudoku_2)
