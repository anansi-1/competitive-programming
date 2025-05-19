# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0
        ans = 0
        curr = 0
        for i in range(len(nums)):
            while curr & nums[i]:
                curr ^= nums[l]
                l += 1
            ans = max(ans, i - l + 1)
            curr  ^= nums[i]
        return ans