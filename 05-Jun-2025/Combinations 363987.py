# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        c = []
        def backtrack(s):
            if len(c) == k:
                ans.append(c[:])
                return    
            for num in range(s, n + 1):
                c.append(num)
                backtrack(num + 1)
                c.pop()
        backtrack(1)
        return ans