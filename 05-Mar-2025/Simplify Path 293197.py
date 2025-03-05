# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        ans = []
        for i in path:
            if i == ".." and len(ans) != 0:
                ans.pop()
            elif i == "" or i == ".." or i == ".":
                continue
            else:
                ans.append(i)
        if len(ans) > 1 and ans[-1]=="/":
            ans.pop()

        return ("/" + "/".join(ans))