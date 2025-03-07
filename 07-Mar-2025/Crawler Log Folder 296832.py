# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = []
        for i in logs:
            if i == "../" and len(ans) != 0:
                ans.pop()
            elif i == "./":
                continue
            elif i != "../":
                ans.append(i)
        return len(ans)