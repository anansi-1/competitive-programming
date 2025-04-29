# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False]*n
        visited[0] = True
        k = set()
        for i in rooms[0]:
            k.add(i)
        while k:
            t = set()
            for i in k:
                if not visited[i]:
                    visited[i] = True
                    for j in rooms[i]:
                        t.add(j)                             
            k= t
        return all(visited)