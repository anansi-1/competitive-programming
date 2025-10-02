# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}

        def fib(n,memo):
            if n==0:
                return 0
            if n<=2:
                return 1
            if n not in memo:
               memo[n]=fib(n-1,memo)+fib(n-2,memo)+fib(n-3,memo)
            return memo [n]

        return(fib(n,memo))