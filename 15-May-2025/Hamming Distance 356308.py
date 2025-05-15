# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        r = x ^ y
        while r:
            if (r&1):
                ans += 1
            r >>= 1
        return ans