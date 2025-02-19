# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        l = 0 
        ans = 0
        for r in range(len(s)):
            if s[r] == "0":
                ans += (r-l)
                l += 1
        return ans