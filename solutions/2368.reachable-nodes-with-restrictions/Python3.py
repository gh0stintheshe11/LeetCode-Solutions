class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        from collections import defaultdict, deque
        
        # Convert restricted list to a set for O(1) access
        restricted_set = set(restricted)
        
        # Construct the graph (adjacency list) from the edges
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # BFS to count the reachable nodes
        queue = deque([0])
        visited = set([0])
        reachable_count = 0
        
        while queue:
            node = queue.popleft()
            reachable_count += 1
            
            for neighbor in graph[node]:
                if neighbor not in visited and neighbor not in restricted_set:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return reachable_count