# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        l = len(arr)
        p = [0] * l
        ans = []
        p[0] = arr[0]
        for i in range(1,l):
            p[i] = p[i-1]^arr[i]
        for l,r in queries:
            if l == 0:
                ans.append(p[r])
            else:
                ans.append(p[r]^p[l-1])
        return ans