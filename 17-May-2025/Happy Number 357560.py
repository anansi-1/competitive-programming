# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:    
        v = set()
        def next_number(n):    
            ans = 0
            while n:
                digit = n % 10
                ans += digit ** 2
                n = n // 10 
            return ans
        while n not in v:
            v.add(n)
            n = next_number(n)
            if n == 1:
                return True
        return False