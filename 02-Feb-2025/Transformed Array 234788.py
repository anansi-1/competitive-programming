# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            index = i + nums[i]
            result.append(nums[index % len(nums)])
        return result