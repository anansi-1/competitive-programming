# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = float("-inf")
        for i in accounts:
            maximum = max(maximum,sum(i))
        return maximum
