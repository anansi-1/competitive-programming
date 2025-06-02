# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        max_heap = []
        for i , row in enumerate(grid):
            sort_row = sorted(row, reverse=True)
            for j in sort_row[:limits[i]]:
                heapq.heappush(max_heap, -j)     
        ans = 0
        min_v = min(k, len(max_heap))
        for i in range(min_v):
            ans += -heapq.heappop(max_heap) 
        return ans