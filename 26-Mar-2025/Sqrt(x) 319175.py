# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 0
        square_root = 0
        hi = x
        while lo <= hi:
            mid = (lo+hi)//2
            if mid*mid <= x:
                square_root = mid
                lo = mid +1
            else:
                hi = mid-1
        return square_root
        