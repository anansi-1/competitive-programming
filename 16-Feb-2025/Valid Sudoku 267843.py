# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s = set()
            for j in range(9):
                num = board[i][j]
                if num in s:
                    return False
                elif num != '.':
                    s.add(num)      
        for i in range(9):
            s = set()
            for j in range(9):
                num = board[j][i]
                if num in s:
                    return False
                elif num != '.':
                    s.add(num)
            
        dirc = [(0, 0), (0, 3), (0, 6),
                  (3, 0), (3, 3), (3, 6),
                  (6, 0), (6, 3), (6, 6)]
        
        for i, j in dirc:
            s = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    num = board[row][col]
                    if num in s:
                        return False
                    elif num != '.':
                        s.add(num)
        return True