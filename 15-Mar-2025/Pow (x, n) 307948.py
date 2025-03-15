# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            curr = power(x,n//2)
            ans = curr * curr
            if n % 2==1:
                return ans*x
            else:
                return ans
        if n < 0:
            return 1/power(x,abs(n))
        else:
            return power(x,n)