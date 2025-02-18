# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        running_sum = 0
        d = defaultdict(int)
        for i in range(len(nums)):
            running_sum += nums[i]
            if (running_sum - k) == 0:
                count += 1
            if (running_sum - k) in d:
                count += d[running_sum - k]
            d[running_sum] += 1
        return count