# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh,rotten = 1,2
        row,col = len(grid),len(grid[0])
        num_fresh = 0
        queue = deque()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == fresh:
                    num_fresh += 1
                elif grid[r][c] == rotten:
                    queue.append((r,c))
        if num_fresh == 0:
            return 0

        def inbound(x,y):
            if 0 <= x <= (len(grid)-1) and 0 <= y <= (len(grid[0])-1):
                return True
            return False

        min = -1
        while queue:
            l = len(queue)
            min += 1
            for i in range(l):
                i,j = queue.popleft()
                for x,y in [(i,j+1),(i,j-1),(i+1,j),(i-1,j)]:
                    if inbound (x,y) and grid[x][y] == fresh:
                        num_fresh -= 1
                        grid[x][y] = 2
                        queue.append((x,y))
                        
        if num_fresh == 0:
            return min
        else: 
            return -1