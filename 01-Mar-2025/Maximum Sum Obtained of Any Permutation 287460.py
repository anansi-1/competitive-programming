# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        arr = [0]* len(nums)
        for s,e in requests:
            arr[s] += 1
            if e+1 < len(nums):
                arr[e+1] -= 1
        for i in range(1,len(arr)):
            arr[i] = arr[i] + arr[i-1] 
        nums.sort()
        arr.sort()
        total_sum = 0
        for i in range(len(nums)):
            total_sum += arr[i]*nums[i] 
        return total_sum % ((10)**9 + 7)