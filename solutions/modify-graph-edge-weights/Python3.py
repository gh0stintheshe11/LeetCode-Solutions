from typing import List
from collections import deque

class Solution:
    # Create adjacency list without the negative weights
    def createAdjacenyList(self, n, edges):
        adjacencyList = [[] for i in range(n)]
        for u, v, w in edges:
            if w != -1:
                adjacencyList[u].append([v, w])
                adjacencyList[v].append([u, w])
        return adjacencyList

    def modifiedGraphEdges(self, n: int, edges: List[List[int]], src: int, dest: int, target: int) -> List[List[int]]:
        INF = float("inf")
        large = 2 * 10**9
        # 1. adjacency list banao without negative weights.
        adjList = self.createAdjacenyList(n, edges)

        def dijkstra():
            dist = [INF for _ in range(n)]
            dist[src] = 0  # Setting source to be zero
            q = deque()
            q.append(src)
            while len(q) > 0:
                u = q.popleft()
                for v, w in adjList[u]:
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        q.append(v)
            return dist

        # 2. fir apply dijkstra.
        dist = dijkstra()

        # 4. ab dekho ki kya shortest distance koi he jo target se kum he, agr he tho empty array return krdo.
        if dist[dest] < target:
            return []

        # 5. Ab dekho koi shortest distance target ke barabr he?
        # Agr he tho jo bache kuche negative weights he usme 2*10^9
        # lagake edges ko return krdo.
        if dist[dest] == target:
            for i in range(len(edges)):
                if edges[i][2] == -1:
                    edges[i][2] = large
            return edges

        # 6. ab ek ek krke negative weights pe traverse krke unko weight 1 assign krdo fir dijkstra lagao.
        for i in range(len(edges)):
            u, v, w = edges[i]
            if w == -1:
                edges[i][2] = 1
                adjList[u].append([v, 1])
                adjList[v].append([u, 1])

                dist = dijkstra()

                # 8. agr koi aaspaas aya he tho uska weight ko target se match krne ki koshish kro.
                # 9. Fir edges me iterate krke negative weights remove krdo.
                if dist[dest] <= target:
                    edges[i][2] += target - dist[dest]
                    for i in range(len(edges)):
                        if edges[i][2] == -1:
                            edges[i][2] = large
                    return edges

        return []