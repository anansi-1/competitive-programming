# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        sum = 0
        rounds = n//3
        for i in range(n-2,-1,-2):
            if rounds > 0:
                sum += piles[i]
            rounds -= 1        
        return sum