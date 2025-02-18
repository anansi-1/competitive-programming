# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(s,l,r): # ro tatx or
            while (l<r):
                if(s[l]==s[r]):
                    l += 1
                    r -=1
                else:
                    return False
            return True        
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return palindrome(s,l+1,r) or palindrome(s,l,r-1)
        return True
        

        