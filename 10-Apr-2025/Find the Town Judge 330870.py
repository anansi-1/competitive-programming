# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int: 
        if n == 1:
            return 1
        indegree = [0]*n
        outdegree = [0]*n
        for a,b in trust:
            indegree[b-1] += 1
            outdegree[a-1] += 1
        print(indegree,outdegree)
        for i in range(n):
            if indegree[i]==n-1 and outdegree[i] == 0:
                return i+1
        return -1