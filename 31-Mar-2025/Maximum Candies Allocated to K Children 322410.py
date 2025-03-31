# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def num_candy(mid):
            count = 0
            for candy in candies:
                count += candy//mid
            # print("count",count,"mid",mid)
            return count
        left = 1
        right = max(candies)
        ans = 0
        while left <= right:
            mid = (right + left)//2
            if num_candy(mid) >= k:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
