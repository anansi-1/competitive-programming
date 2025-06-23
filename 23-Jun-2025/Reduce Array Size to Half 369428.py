# Problem: Reduce Array Size to Half - https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        count = Counter(arr)
        freq = list(count.values())
        freq.sort(reverse=True)
        left = len(arr)
        res = 0
        for f in freq:
            left -= f
            res += 1
            if left <= len(arr) // 2:
                break
        return res