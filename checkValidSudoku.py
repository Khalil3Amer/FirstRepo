"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""


class Solution:
    def isValidSudoku(self, board) -> bool:
        # check rows
        for row in board:
            for i in range(10):
                if row.count(str(i)) > 1:
                    return False
        # check cols
        for i in range(9):
            li = list(map(lambda x: str(x), range(1, 10)))
            for j in range(9):
                if board[j][i] in li:
                    li.remove(board[j][i])
                elif board[j][i] != ".":
                    return False
        # check 3X3
        li = []
        for z in range(0, 7, 3):
            for w in range(0, 7, 3):
                li = []
                for i in range(z, z + 3):
                    li.append([j for j in board[i][w : w + 3]])
                print(li)
                li1 = list(map(lambda x: str(x), range(1, 10)))
                for i in range(3):
                    for j in range(3):
                        if li[j][i] in li1:
                            print(li[j][i], end="")
                            li1.remove(li[j][i])
                        elif li[j][i] != ".":
                            return False
                    print(li1)
        return True
