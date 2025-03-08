# Problem: Maximum Matching of Players With Trainers - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        trainers.sort()
        players.sort()
        count = 0
        p = 0
        t = 0
        while t < len(trainers) and p < len(players):
            if trainers[t] >= players[p]:
                count +=1
                p += 1
            t +=1
        return count
            