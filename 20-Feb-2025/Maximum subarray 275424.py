# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        
        
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]

        max_sum = float('-inf')
        min_prefix = 0  
        for j in range(1, n + 1):
            max_sum = max(max_sum, prefix[j] - min_prefix)
            min_prefix = min(min_prefix, prefix[j])

        return max_sum