from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0
        
        # Initialize the queue with all nodes and their corresponding bitmasks
        queue = deque((i, 1 << i) for i in range(n))
        visited = set((i, 1 << i) for i in range(n))
        
        steps = 0
        while queue:
            for _ in range(len(queue)):
                node, mask = queue.popleft()
                
                # If all nodes are visited, return the number of steps
                if mask == (1 << n) - 1:
                    return steps
                
                # Explore all neighbors
                for neighbor in graph[node]:
                    new_mask = mask | (1 << neighbor)
                    new_state = (neighbor, new_mask)
                    
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append(new_state)
            
            steps += 1
        
        return -1  # This line should never be reached