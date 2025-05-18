# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        x = 1 << n
        for i in range(x):
            cur = []
            for j in range(n):
                if i& (1<<j):
                    cur.append(nums[j])
            ans.append(cur)
        return ans