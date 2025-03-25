# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        first_bad = 0
        l,r = 1,n
        while l <= r:
            mid = (l + r)//2
            if isBadVersion(mid):
                first_bad = mid
                r = mid - 1
            else:
                l = mid + 1
        return first_bad
