class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        from collections import defaultdict, deque
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        
        state = {}
        
        def dfs(node):
            if node in state:
                return state[node]
            if node not in graph:
                return node == destination
            state[node] = False
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            state[node] = True
            return True
        
        return dfs(source)