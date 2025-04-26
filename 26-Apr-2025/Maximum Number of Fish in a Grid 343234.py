# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def bfs(queue,curr_count):
            while queue:
                x,y = queue.popleft()
                curr_count[0] += grid[x][y]
                grid[x][y] = 0
                for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if (0 <= i < len(grid) and 0 <= j < len(grid[0])) and grid[i][j] > 0:
                        queue.append((i,j))

        queue = deque()
        row,col = len(grid),len(grid[0])
        count = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] > 0:
                    queue.append((i,j))
                    curr_count = [0]
                    bfs(queue,curr_count)
                    count = max(count,curr_count[0])
        
        return count