# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        def find(x: int) -> None:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x: int, y: int) -> bool:
            rootX = find(x)
            rootY = find(y)
            if rank[rootX] >= rank[rootY]:
                parent[rootX] = rootY
                rank[rootX] += rank[rootY]
            else:
                parent[rootY] = rootX
                rank[rootY] += rank[rootX]
            if rootX == rootY:
                return False
            parent[rootX] = rootY
            return True
        
        for edge in edges:
            if not union(edge[0], edge[1]):
                return edge
        return []