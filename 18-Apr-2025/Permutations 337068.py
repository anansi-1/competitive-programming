# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        ans = []
        def backtrack(path,seen):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            for i in range(len(nums)):
                if not seen[i]:
                    seen[i] = True
                    path.append(nums[i])
                    backtrack(path,seen)
                    path.pop()
                    seen[i] = False 
        backtrack([],[False]*len(nums))
        return ans