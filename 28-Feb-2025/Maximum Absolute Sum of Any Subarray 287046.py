# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix_sum = []
        running_sum = 0
        for i in range(0,len(nums)):
            running_sum += nums[i]
            prefix_sum.append(running_sum)
        min_sum = 0 
        max_sum = float('-inf')
        for i in range(len(prefix_sum)):
            max_sum = max(max_sum,prefix_sum[i]-min_sum)
            min_sum = min(min_sum,prefix_sum[i])
        max_p = 0
        minn = float('inf')
        for i in range(len(prefix_sum)):
            minn = min(minn,prefix_sum[i]-max_p)
            max_p = max(max_p,prefix_sum[i])
        minn = abs(minn)
        max_sum = abs(max_sum)
        return max(minn,max_sum)