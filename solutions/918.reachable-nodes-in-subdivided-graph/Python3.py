import heapq
from typing import List

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = {i: {} for i in range(n)}
        for u, v, cnt in edges:
            graph[u][v] = cnt
            graph[v][u] = cnt
        
        pq = [(0, 0)]
        dist = {0: 0}
        visited = set()
        
        while pq:
            moves, node = heapq.heappop(pq)
            if moves > maxMoves or node in visited:
                continue
            visited.add(node)
            for neighbor, cnt in graph[node].items():
                next_moves = moves + cnt + 1
                if next_moves <= maxMoves and (neighbor not in dist or next_moves < dist[neighbor]):
                    dist[neighbor] = next_moves
                    heapq.heappush(pq, (next_moves, neighbor))
        
        result = len(visited)
        for u, v, cnt in edges:
            reach_from_u = max(0, maxMoves - dist.get(u, maxMoves + 1))
            reach_from_v = max(0, maxMoves - dist.get(v, maxMoves + 1))
            result += min(cnt, reach_from_u + reach_from_v)
        
        return result