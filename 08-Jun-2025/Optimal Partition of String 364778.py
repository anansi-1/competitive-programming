# Problem: Optimal Partition of String - https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        c=0
        st=""
        for i in range(len(s)):
            if s[i] in st:
                c+=1
                st=s[i]  
            else:
                st+=s[i]
        if st: 
            c+=1
        return c