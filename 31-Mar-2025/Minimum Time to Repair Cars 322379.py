# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def get_car(mid):
            curr_cars = 0
            for mech in ranks:
                curr_cars += int(sqrt(mid/mech))
            return curr_cars
        ans = 0
        min_time = 1
        max_time = max(ranks)*(cars*cars)
        while min_time <= max_time:
            mid = (min_time + max_time)//2
            if get_car(mid) >= cars:
                ans = mid
                max_time = mid - 1
            else:
                min_time = mid + 1
        return ans