# QUESTION:
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# 1. Each row must contain the digits 1-9 without repetition.
# 2. Each column must contain the digits 1-9 without repetition.
# 3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        current = set()
        for y in range(9):
            for x in range(9):
                if board[y][x] == '.':
                    continue
                row = f'#{board[y][x]} in row #{x}'
                if row in current:
                    return False
                current.add(row)
                column = f'#{board[y][x]} in column #{y}'
                if column in current:
                    return False
                current.add(column)
                square = f'#{board[y][x]} in square #{x // 3}#{y // 3}'
                if square in current:
                    return False
                current.add(square)
        return True
