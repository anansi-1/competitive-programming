# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        s = []
        for idx,val in enumerate(temperatures):
            while s and val > s[-1][1]:
                ans[s[-1][0]] = idx - s[-1][0]
                s.pop() 
            s.append((idx,val))
        return ans