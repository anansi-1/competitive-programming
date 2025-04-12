# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def countBalls(d):
            balls, cur = 1, position[0]
            for i in range(1,len(position)):
                if position[i] - cur >=d:
                    balls += 1
                    cur = position[i]
            return balls        
        left = 1
        right = max(position) - min(position)

        while left <= right:
            mid = (left+right)//2
            if countBalls(mid) >= m:
                left = mid+1
            else:
                right = mid - 1
        return right