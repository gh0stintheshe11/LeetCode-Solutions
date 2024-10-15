from typing import List
import heapq

class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        n = len(scores)
        graph = [[] for _ in range(n)]
        
        # Build Graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Retain only top 3 highest scoring neighbors
        def top_k_neighbors(node):
            return heapq.nlargest(3, graph[node], key=lambda x: scores[x])
        
        # Filter graph to top scoring connections
        top_neighbors = [top_k_neighbors(i) for i in range(n)]
        
        max_score = -1
        
        for u, v in edges:
            neighbors_u = top_neighbors[u]
            neighbors_v = top_neighbors[v]
            
            for nu in neighbors_u:
                if nu == v or nu == u:
                    continue
                for nv in neighbors_v:
                    if nv == u or nv == v or nv == nu:
                        continue
                    max_score = max(max_score, scores[u] + scores[v] + scores[nu] + scores[nv])
        
        return max_score