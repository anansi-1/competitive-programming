# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        count = defaultdict(int)
        for u, v in edges:
            count[v] += 1
        ans, t = 0, 0
        for i in range(n):
            if not count[i]:
                ans = i
                t += 1
            if t == 2:
                return -1
        return ans