from collections import deque, defaultdict
from typing import List, Tuple

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def compute_time(current_time: int, time: int, change: int) -> int:
            if (current_time // change) % 2 == 1:  # If red light
                current_time = (current_time // change + 1) * change  # Wait until green
            return current_time + time
        
        # BFS for shortest and second shortest paths
        first_arrival = [float('inf')] * (n + 1)
        second_arrival = [float('inf')] * (n + 1)
        
        q = deque([(1, 0)])
        first_arrival[1] = 0
        
        while q:
            node, curr_time = q.popleft()
            
            for neighbor in graph[node]:
                new_time = compute_time(curr_time, time, change)
                
                if new_time < first_arrival[neighbor]:
                    second_arrival[neighbor] = first_arrival[neighbor]
                    first_arrival[neighbor] = new_time
                    q.append((neighbor, new_time))
                elif first_arrival[neighbor] < new_time < second_arrival[neighbor]:
                    second_arrival[neighbor] = new_time
                    q.append((neighbor, new_time))
        
        return second_arrival[n]