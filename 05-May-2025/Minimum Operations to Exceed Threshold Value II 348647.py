# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heapq.heapify(nums)
        m = 0
        while len(nums) > 1 and nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            val = 2 * min(x, y) + max(x, y)
            heapq.heappush(nums, val)
            m += 1
        if nums and nums[0] >= k:
            return m
        return -1
