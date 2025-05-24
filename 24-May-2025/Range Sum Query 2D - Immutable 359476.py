# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        self.prefix = [[0] * (len(matrix[0]) + 1) for i in range(len(matrix) + 1)]
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                self.prefix[i][j] = matrix[i-1][j-1] + self.prefix[i-1][j] + self.prefix[i][j-1] - self.prefix[i-1][j-1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        t = self.prefix[row2 + 1][col2 + 1]
        a = self.prefix[row1][col2 + 1]
        l = self.prefix[row2 + 1][col1]
        over = self.prefix[row1][col1]
        return t - a - l + over



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)