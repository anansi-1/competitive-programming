# Problem: Find the Duplicate Number - https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = -1
        l, h = 1, len(nums) -1
        while l <= h:
            mid = l + (h - l) // 2
            less_nums_count = 0
            for num in nums:
                if num <= mid:
                    less_nums_count += 1
            if less_nums_count > mid:
                d = mid
                h = mid - 1 
            else:
                l = mid + 1
        return d