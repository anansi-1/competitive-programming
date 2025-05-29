# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        res = 0
        heater = 0   
        for h in houses:
            while heater + 1 < len(heaters) and heaters[heater + 1] == heaters[heater]:                
                heater += 1
            while heater + 1 < len(heaters) and abs(heaters[heater + 1] - h) < abs(heaters[heater] - h): 
                heater += 1                                                                           
            res = max(res, abs(heaters[heater] - h))    
        return res