# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = {}
        loser = {}

        for i in range(len(matches)):
            winner[matches[i][0]] = winner.get(matches[i][0], 0) + 1
            loser[matches[i][1]] = loser.get(matches[i][1], 0) + 1

        zero_losses = []
        for player in winner:
            if player not in loser:
                zero_losses.append(player)
        one_loss = []

        for player,count in loser.items():
            if count == 1:
                one_loss.append(player)
        
        zero_losses.sort()
        one_loss.sort()

        return [zero_losses, one_loss]