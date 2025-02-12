# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_stored = float('-inf')
        while l < r:
            cur_width = r - l
            cur_height = min(height[l],height[r])
            cur_stored = cur_height * cur_width
            max_stored = max(max_stored,cur_stored)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_stored