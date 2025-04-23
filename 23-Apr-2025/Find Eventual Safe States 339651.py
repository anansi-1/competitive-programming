# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        indeg = defaultdict(int)
        new_graph = defaultdict(list)
        n = len(graph)
        for node in range(n):
            for nei in graph[node]:
                new_graph[nei].append(node)
                indeg[node] += 1
        queue = deque()
        for node in range(n):
            if indeg[node] == 0:
                queue.append(node)
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for nei in new_graph[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    queue.append(nei)

        return sorted(order)
