# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque()
        for i in range(1,n+1):
            queue.append(i)
        while len(queue) > 1:
            for i in range(k-1):
                curr = queue.popleft()
                queue.append(curr)
            queue.popleft()
        return queue[-1]
