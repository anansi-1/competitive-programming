# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        a = [0]
        while(len(a) <= n):
            a += [i + 1 for i in a]
        return a[:n+1]