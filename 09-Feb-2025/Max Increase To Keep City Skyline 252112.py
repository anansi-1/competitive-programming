# Problem: Max Increase To Keep City Skyline - https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = [[0]*cols for _ in range(rows)]
        #  0  1  2  3 
        # [8, 7, 9, 3]--row
        # [9, 4, 8, 7]--col

        row_max = []
        for row in grid:
            row_max.append(max(row))
        col_max = []
        for col in range(cols):
            max_c = float('-inf')
            for row in range(-1,rows-1):
                max_c = max(max_c,grid[row][col])
            col_max.append(max_c)
        max_total_sum = 0
        for i in range(rows):
            for j in range(cols):
                to_add = min((row_max[i],col_max[j])) -grid[i][j]
                max_total_sum += to_add 
        return max_total_sum