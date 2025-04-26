# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c,visited):
            if (r,c) not in visited and grid[r][c] == "1":
                visited.add((r,c))
                for i,j in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    if 0 <= i <= (len(grid)-1) and 0 <= j <= (len(grid[0])-1):
                        dfs(i,j,visited)
        visited = set()
        row,col = len(grid),len(grid[0])
        count = 0

        for i in range(row):
            for j in range(col):
                if (i,j) not in visited and grid[i][j] == "1":
                    count += 1
                    dfs(i,j,visited)
        return count