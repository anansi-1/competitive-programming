# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
            def dfs(r,c,curr_count):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                for i,j in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                        if (0 <= i < len(grid) and 0 <= j < len(grid[0])) and grid[i][j] == 1:
                                curr_count[0] += 1
                                dfs(i,j,curr_count)
                        
            row,col = len(grid),len(grid[0])
            count = float('-inf')

            for i in range(row):
                for j in range(col):
                    if grid[i][j] == 1:
                        curr_count = [1]
                        dfs(i,j,curr_count)
                        count = max(count,curr_count[0])
                                
            return count if count != float('-inf') else 0