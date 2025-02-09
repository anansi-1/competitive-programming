# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        maxLocal_col = len(grid[0]) -2
        maxLocal_row = len(grid) -2
        maxLocal = [[0]*maxLocal_col for _ in range(maxLocal_row)]

        for row in range(maxLocal_row):
            for col in range(maxLocal_col):
                r = row+1
                c = col+1
                local_max = float('-inf')
                for i in (r-1,r,r+1):
                    for j in (c-1,c,c+1):
                        local_max = max(local_max,grid[i][j])
                maxLocal[row][col] = local_max
        return maxLocal