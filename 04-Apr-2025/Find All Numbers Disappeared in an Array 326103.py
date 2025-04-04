# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        ans = []
        while i < n:
            p = nums[i] - 1
            if p != i and nums[p] != nums[i]:
                nums[p],nums[i] = nums[i],nums[p]
            else:
                i += 1

        for i in range(n):
            if i + 1 != nums[i]:
                ans.append(i+1)
        return ans                