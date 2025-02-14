# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        l = 0
        for r in range(len(s1),len(s2)+1):
            cur_window = sorted(s2[l:r])
            if s1 == cur_window:
                return True
            l += 1
        return False