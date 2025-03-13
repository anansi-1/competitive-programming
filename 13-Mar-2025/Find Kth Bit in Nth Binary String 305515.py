# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(n):
            arr = []
            if n == 1:
                return "0"
            prev =  helper(n-1)

            for i in prev:
                if i == "0":
                    arr.append("1")
                else:
                    arr.append("0")
            arr.reverse()
            return prev  + "1" + "".join(arr)
        ans = helper(n)
        return ans[k-1]