# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if f"{nums[j]}{nums[i]}" > f"{nums[i]}{nums[j]}":
                    nums[i],nums[j] = nums[j],nums[i]
        if nums[0] ==0:
            return "0"
        return "".join(map(str,nums))