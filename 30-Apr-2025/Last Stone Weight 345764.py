# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        i,j = len(stones) - 2, len(stones) - 1
        while j > 0:
            stones.sort()
            if stones[i] == stones[j]:
                stones.pop()
                stones.pop()
                i -= 2
                j -= 2
            elif stones[i] < stones[j]:
                stones[i] = stones[j] - stones[i]
                stones.pop()
                i -= 1
                j -= 1
        return stones[0] if stones else 0