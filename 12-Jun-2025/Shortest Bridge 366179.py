# Problem: Shortest Bridge - https://leetcode.com/problems/shortest-bridge/

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        di = [[-1,0],[1,0],[0,-1],[0,1]]
        n = len(grid)
        que = deque()
        visited = set()
        def bfs(r,c):
            que.append([0,r,c])
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                ro,co=q.popleft()
                grid[ro][co] = 2
                for sr,sc in di:
                    row = ro+sr
                    col = co+sc
                    if min(row,col)>=0 and max(row,col)<n and (row,col) not in visited and grid[row][col]==1:
                        visited.add((row,col))
                        que.append([0,row,col])
                        q.append((row,col))
            return 
        count = 0
        for i in range(n):
            for j in range(n):
                if count == 0 and grid[i][j] == 1:
                    bfs(i,j)
                    count += 1
                    break
            if count == 1:
                break                
        while  que:
            dis ,r,c = que.popleft()
            for sr,sc in di:
                row = r+sr
                col = c+sc        
                if min(row,col)>=0 and max(row,col)<n and (row,col) not in visited:
                    if grid[row][col] == 1:
                        return dis
                    que.append([dis+1,row,col]) 
                    visited.add((row,col))    
        return -1