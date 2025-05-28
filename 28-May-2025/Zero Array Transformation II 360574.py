# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n= len(nums)
        q = len(queries)
        l, r = 0,q
        def canZeroArray(k):
            diffArr = [0 for _ in range(n+1)]
            for s, e, val in queries[0:k]:
                diffArr[s] += val
                diffArr[e+1] -= val
            count = 0
            for i in range(n+1):
                change = diffArr[i]
                diffArr[i] += count
                count += change
            for i, v in enumerate(nums):
                if v > diffArr[i]:
                    return False
            return True         
        while l < r:
            mid = (l + r) // 2
            if canZeroArray(mid):
                r = mid
            else:
                l = mid + 1
        mid = (l + r) // 2
        if mid < q+1 and not canZeroArray(mid):
            mid += 1
        if mid == q+1:
            return -1
        return mid