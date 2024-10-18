import heapq
from typing import List

class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        def manhattan(x1, y1, x2, y2):
            return abs(x2 - x1) + abs(y2 - y1)

        nodes = [(start[0], start[1]), (target[0], target[1])]
        for x1, y1, x2, y2, _ in specialRoads:
            nodes.append((x1, y1))
            nodes.append((x2, y2))
    
        nodes = list(set(nodes))
        node_index = {node: i for i, node in enumerate(nodes)}
        
        graph = {node: {} for node in nodes}
        
        for x1, y1, x2, y2, cost in specialRoads:
            graph[(x1, y1)][(x2, y2)] = min(graph[(x1, y1)].get((x2, y2), float('inf')), cost)
        
        start_node = (start[0], start[1])
        target_node = (target[0], target[1])
        
        pq = [(0, node_index[start_node])]
        costs = {i: float('inf') for i in range(len(nodes))}
        costs[node_index[start_node]] = 0
        
        while pq:
            current_cost, current = heapq.heappop(pq)
            if current == node_index[target_node]:
                return current_cost
            
            x1, y1 = nodes[current]
            for x2, y2 in nodes:
                next_node = (x2, y2)
                next_index = node_index[next_node]
                step_cost = manhattan(x1, y1, x2, y2)
                if next_node in graph[(x1, y1)]:
                    step_cost = min(step_cost, graph[(x1, y1)][next_node])
                
                new_cost = current_cost + step_cost
                if new_cost < costs[next_index]:
                    costs[next_index] = new_cost
                    heapq.heappush(pq, (new_cost, next_index))
        
        return costs[node_index[target_node]]