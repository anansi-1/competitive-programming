# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        ans = []
        while i < n:
            p = nums[i] - 1
            if nums[p] != nums[i]:
                nums[p],nums[i] = nums[i],nums[p]
            else:
                i += 1
        for i in range(n):
            if i + 1 != nums[i]:
                return [nums[i], i + 1] 
        