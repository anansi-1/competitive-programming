# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def gives_hours(piles,rate):
            hour_taken = 0
            for bananas in piles:
                hour_taken += ceil(bananas/rate)
            return hour_taken

        ans = 0
        min_rate = 1
        max_rate = sum(piles)
        while min_rate <= max_rate:
            mid = (min_rate + max_rate)//2
            if gives_hours(piles,mid) <= h:
                ans = mid
                max_rate = mid - 1
            else:
                min_rate = mid + 1
        return ans