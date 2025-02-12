# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 1
        while right < len(nums):
            if nums[right] != 0 and nums[left] ==0:
                nums[right],nums[left]=nums[left],nums[right]
                right += 1
                left += 1
            elif nums[left] ==0 and nums[right] ==0:
                right+=1
            else:
                right += 1
                left += 1