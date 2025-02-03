# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(max(nums)+1):  
            if i in nums:
                continue
            else:
                return i
        return max(nums) + 1
        