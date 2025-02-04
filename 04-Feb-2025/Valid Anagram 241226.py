# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if sorted(s)== sorted(t):
        #     return True
        # return False
        s = Counter(s)
        t = Counter(t)
        if Counter(s) == Counter(t):
            return True
        return False