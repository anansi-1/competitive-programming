# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(num):
            if num == 1 or num ==0:
                return 1
            else:
                return num * factorial(num-1)
        ans = (factorial(n))
        count = 0
        while ans%10 == 0:
            count += 1
            ans = ans//10
        return count