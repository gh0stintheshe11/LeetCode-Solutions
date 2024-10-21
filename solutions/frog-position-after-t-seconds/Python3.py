class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        from collections import defaultdict

        # Build the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node, parent, current_time, probability):
            # If the target is reached and we have not exhausted time, or if the node has no other moves:
            if current_time == t:
                if node == target:
                    return probability
                return 0.0
            if node == target:
                if len(graph[node]) == (1 if parent else 0):
                    return probability
                return 0.0
                
            # Counting the unvisited children (exclude the parent)
            unvisited_count = len(graph[node]) - (0 if parent is None else 1)
            if unvisited_count == 0:
                return 0.0  # No further moves possible and time still left
            
            prob_per_child = probability / unvisited_count
            for neighbor in graph[node]:
                if neighbor != parent:
                    res = dfs(neighbor, node, current_time + 1, prob_per_child)
                    if res > 0:
                        return res
            
            return 0.0
        
        return dfs(1, None, 0, 1.0)