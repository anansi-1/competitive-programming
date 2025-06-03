# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        ans = [[-1 for j in range(n)] for i in range(m)]
        q = deque()
        for r in range(m):
            for c in range(n):
                if isWater[r][c] == 1:
                    ans[r][c] = 0
                    q.append((r, c))
        while q:
            r, c = q.popleft()
            for i , j in direction:
                x, y = r + i, c + j
                if 0 <= x < m and 0 <= y < n and ans[x][y] == -1:
                    ans[x][y] = ans[r][c] + 1
                    q.append((x, y))
        return ans