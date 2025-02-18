# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        running_sum = 0
        d = defaultdict(int)
        for i in range(len(nums)):
            running_sum += nums[i]
            if (running_sum - goal) == 0:
                count += 1
            if (running_sum - goal) in d:
                count += d[running_sum - goal]
            d[running_sum] += 1
        return count