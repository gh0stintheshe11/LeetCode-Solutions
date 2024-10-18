class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        from collections import defaultdict, deque

        graph = defaultdict(list)
        
        # Build the graph
        for a, b, d in roads:
            graph[a].append((b, d))
            graph[b].append((a, d))
        
        # BFS to find the connected component that contains 1
        visited = set()
        queue = deque([1])
        
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                for neighbor, _ in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        # Find the minimum score in the connected component
        min_score = float('inf')
        for node in visited:
            for neighbor, distance in graph[node]:
                min_score = min(min_score, distance)
        
        return min_score