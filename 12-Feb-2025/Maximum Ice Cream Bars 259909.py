# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n = max(costs) + 1  
        freq_arr = [0]*n  
        for i in costs:
            freq_arr[i] += 1
        ice_cream = 0
        for i in range(1,len(freq_arr)):
            j = freq_arr[i]
            while j > 0:
                coins -= i
                j -= 1
                if coins >=0:
                    ice_cream += 1
                else:
                    break
        return ice_cream