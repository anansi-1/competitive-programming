# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ans_s = []
        ans_t = []
        for i in s:
            if i == "#" and len(ans_s) != 0:
                ans_s.pop()
            elif i != "#":
                ans_s.append(i)
        for i in t:
            if i == "#" and len(ans_t) != 0:
                ans_t.pop()
            elif i != "#":
                ans_t.append(i)
        if ans_t == ans_s :
            return True
        else: 
            return False