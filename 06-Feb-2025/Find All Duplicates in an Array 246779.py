# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        nums = Counter(nums)
        for i in nums:
            if nums[i] > 1:
                ans.append(i)
        return ans