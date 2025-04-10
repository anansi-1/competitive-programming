# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        seen = set()
        adj_list = defaultdict(list)
        for node,adj in edges:
            adj_list[node].append(adj)
            adj_list[adj].append(node)
        def dfs(node):
            seen.add(node)
            if node == destination:
                return True
 
            for i in adj_list[node]:
                if i not in seen:
                    if dfs(i):
                        return True
            return False
        
        return dfs(source)