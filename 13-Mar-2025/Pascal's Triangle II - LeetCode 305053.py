# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        else:
            prev = self.getRow(rowIndex-1)
            curr= [1]
        
        for i in range(1,rowIndex):
            curr.append(prev[i]+prev[i-1])
             
        curr.append(1)
        return curr