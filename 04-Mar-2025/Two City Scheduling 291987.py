# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        diff = []
        for cost in costs:
            diff.append((cost[0]-cost[1])) 
        curr_total =0
        for i in range(len(costs)):
            curr_total += costs[i][0]
        diff.sort(reverse=True)
        curr_total -= sum(diff[:n//2])
        return (curr_total)