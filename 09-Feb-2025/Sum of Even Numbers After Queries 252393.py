# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even = 0
        for value in nums:
            if value % 2 == 0:
                even += value
        res = []
        for val, i in queries:
            if nums[i] % 2 == 0:
                even -= nums[i]
            nums[i] += val
            if nums[i] % 2 == 0:
                even += nums[i]
            res.append(even)
        return res