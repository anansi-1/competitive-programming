# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        block = False
        ans = []
        new = []
        for line in source:
            if not block:
                new = []
            i = 0
            while i < len(line):
                if line[i : i + 2] == '/*' and not block:
                    block = True
                    i += 1
                elif line[i : i + 2] == '*/' and block:
                    block = False
                    i += 1
                elif line[i : i + 2] == '//' and not block:
                    break
                elif not block:
                    new.append(line[i])
                i += 1
            if new and not block:
                ans.append(''.join(new))
        return ans