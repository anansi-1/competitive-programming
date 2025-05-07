# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights)-1):
            c = heights[i+1] - heights[i]
            if c > 0:
                bricks -= c
                heapq.heappush(heap,-c)
                if bricks < 0:
                    if ladders == 0:
                        return i
                    ladders -= 1
                    bricks += - heapq.heappop(heap)
        return len(heights) - 1