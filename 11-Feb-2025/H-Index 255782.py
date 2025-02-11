# Problem: H-Index - https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort() # [0,1,3,5,6]
        for i in range(n):
            if citations[i] >= n:
                return n
            n -= 1
        return 0
