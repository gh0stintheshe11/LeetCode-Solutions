from typing import List
import heapq

class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        graph = [[] for _ in range(n)]
        
        for u, v, cost in highways:
            graph[u].append((v, cost))
            graph[v].append((u, cost))
        
        # Priority queue for Dijkstra's (cost, node, remaining discounts)
        heap = [(0, 0, discounts)]
        # Best cost to reach each node with a specific number of discounts
        best_cost = [[float('inf')] * (discounts + 1) for _ in range(n)]
        best_cost[0][discounts] = 0
        
        while heap:
            curr_cost, node, rem_discounts = heapq.heappop(heap)
            
            if node == n - 1:
                return curr_cost
            
            if curr_cost > best_cost[node][rem_discounts]:
                continue
            
            for neighbor, toll in graph[node]:
                new_cost = curr_cost + toll
                if new_cost < best_cost[neighbor][rem_discounts]:
                    best_cost[neighbor][rem_discounts] = new_cost
                    heapq.heappush(heap, (new_cost, neighbor, rem_discounts))
                
                if rem_discounts > 0:
                    discount_cost = curr_cost + toll // 2
                    if discount_cost < best_cost[neighbor][rem_discounts - 1]:
                        best_cost[neighbor][rem_discounts - 1] = discount_cost
                        heapq.heappush(heap, (discount_cost, neighbor, rem_discounts - 1))
        
        return -1