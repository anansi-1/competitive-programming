# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        group = [0] * len(graph)
        for i in range(len(graph)):
            if group[i] != 0: 
                continue 
            group[i] = 1
            queue = deque([i])
            while queue:
                node = queue.popleft()
                for neighbour in graph[node]:
                    if group[neighbour] == 0:
                        group[neighbour] = -group[node]
                        queue.append(neighbour)
                    else: 
                        if group[neighbour] == group[node]:
                            return False  
        return True 