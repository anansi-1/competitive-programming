# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        count = defaultdict(int)
        for i in arr:
            r = i % k
            count[r] += 1
        for r in range(k//2 + 1):
            if r == 0:
                if count[r] % 2 != 0:
                    return False
            else: 
                if count[r] != count[k-r]:
                    return False
        return True