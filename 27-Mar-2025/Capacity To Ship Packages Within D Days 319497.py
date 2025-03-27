# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def give_days(capacity,weights):
            load = 0
            days = 0
            for weight in weights:
                if (load+weight) > capacity:
                    days += 1
                    load = weight
                else:
                    load += weight
            return days + 1
        ans = 0
        min_capacity = max(weights)
        max_capacity = sum(weights)
        while min_capacity <= max_capacity:
            mid = (min_capacity + max_capacity)//2
            if give_days(mid,weights) <= days:
                ans = mid
                max_capacity = mid - 1
            else:
                min_capacity = mid + 1
        return ans