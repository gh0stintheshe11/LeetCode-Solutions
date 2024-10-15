from collections import deque
from typing import List

class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        graph = [[] for _ in range(n)]
        
        # Building the graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Find the shortest path to each node from the master server (node 0)
        dist = [float('inf')] * n
        dist[0] = 0
        queue = deque([0])
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if dist[neighbor] == float('inf'):
                    dist[neighbor] = dist[node] + 1
                    queue.append(neighbor)
        
        # Calculating the time when network becomes idle
        max_time = 0
        for i in range(1, n):
            round_trip_time = 2 * dist[i]
            last_send_time = (round_trip_time - 1) // patience[i] * patience[i]
            last_arrival_time = last_send_time + round_trip_time
            max_time = max(max_time, last_arrival_time)
        
        return max_time + 1