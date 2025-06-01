# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        for e, m in enumerate(manager):
            if m != -1:
                adj[m].append(e)
        res = 0
        q = deque([(headID, informTime[headID])])
        while q:
            m, t = q.popleft()
            res = max(res, t)
            for i in adj[m]:
                q.append((i, t + informTime[i]))
        return res