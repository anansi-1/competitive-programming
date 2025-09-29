# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n = len(cost)
        if n == 2:
            return max(cost[0], cost[1])
        else:
            for i in range((n-3),-1,-1):
                cost[i] += min(cost[i+1], cost[i+2])
            return min(cost[i], cost[i+1])