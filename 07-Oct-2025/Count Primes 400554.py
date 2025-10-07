# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True]*(n+1)
        count = 0
        if n == 0 or n ==1:
            return 0
        for i in range(2,n//2 + 1):
            if prime[i]==True:
                count += 1
                for j in range(2*i, n+1,i):
                    prime[j] = False
        for i in range((n//2)+1,n+1):
            if i <n and prime[i] == True :
                count += 1         
        return count