# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = max(nums) 
        m = min(nums) 
        multi = (n - m) + 1
        count = [0] * multi
        res = []
        count = [0]*multi
        for num in nums:
            count[num- m] += 1
        for i in range(len(count)):
            for j in range(count[i]):
                ans = i + m
                res.append(ans)
        return res
