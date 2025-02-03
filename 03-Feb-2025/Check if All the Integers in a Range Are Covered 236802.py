# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        nums = set()
        for arr in ranges:
            for i in range(arr[-1],arr[0]-1,-1):
                nums.add(i)
        for i in range(left,right+1):
            if i not in nums:
                return False
        return True