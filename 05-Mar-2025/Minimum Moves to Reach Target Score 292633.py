# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
            if target == 1:
                return 0
            if maxDoubles ==0:
                return target - 1
            min_steps = 0
            while target != 1 and maxDoubles != 0:
                if target%2 != 0:
                    target = target //2
                    maxDoubles -= 1
                    min_steps += 2
                else:
                    target = target //2
                    maxDoubles -= 1
                    min_steps += 1
            if target != 1:
                min_steps += target - 1
            return min_steps