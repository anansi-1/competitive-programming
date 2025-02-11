# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        occur = {}
        for i in s:
            occur[i] = occur.get(i,0) + 1
        occur_pair = sorted(occur.items(),key=lambda x:x[1],reverse=True)
        ans = []
        for k,v in occur_pair:
            ans.append(k*v)
        return "".join(ans)