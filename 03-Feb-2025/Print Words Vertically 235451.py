# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        ans = []
        max_len = 0
        for i in s:
            max_len = (max(max_len,len(i)))
        for i in range(max_len):
            word = []
            for j in range(len(s)):
                if i >= len(s[j]):
                    word.append(" ")
                else:
                    word.append(s[j][i])
            ans.append(("".join(word)).rstrip())
        return ans