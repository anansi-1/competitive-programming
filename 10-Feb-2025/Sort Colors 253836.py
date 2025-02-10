# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(i+1):
                if nums[i] < nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]
        return nums