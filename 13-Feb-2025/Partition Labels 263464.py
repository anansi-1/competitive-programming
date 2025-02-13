# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occur = {}
        for i in range(len(s)-1,-1,-1):
            if s[i] not in last_occur:
                last_occur[s[i]] = i
        ans = []
        l = 0
        r = 0
        for i in range(len(s)):
            r = max(r,last_occur[s[i]])
            if i == r:
                ans.append(r-l+1)
                l = i + 1
        return ans