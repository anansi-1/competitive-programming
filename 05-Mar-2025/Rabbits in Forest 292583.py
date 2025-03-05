# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        min_rabbit = 0
        for key,value in count.items():
            if key == 0:
                min_rabbit += value
            else:
                curr = value//(key+1)
                min_rabbit += curr * (key+1)
                r = value % (key+1)
                if r > 0:
                    min_rabbit += key + 1
                r = 0
        return min_rabbit