import heapq
from collections import defaultdict, deque

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7

        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def dijkstra(start):
            dist = {i: float('inf') for i in range(1, n+1)}
            dist[start] = 0
            min_heap = [(0, start)]  # (distance, node)

            while min_heap:
                curr_dist, u = heapq.heappop(min_heap)
                if curr_dist > dist[u]:
                    continue

                for v, weight in graph[u]:
                    if dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight
                        heapq.heappush(min_heap, (dist[v], v))
            return dist

        dist_to_n = dijkstra(n)

        adj_list = defaultdict(list)
        for u in range(1, n+1):
            for v, _ in graph[u]:
                if dist_to_n[u] > dist_to_n[v]:
                    adj_list[u].append(v)

        dp = [-1] * (n + 1)
        dp[n] = 1

        def dfs(node):
            if dp[node] != -1:
                return dp[node]

            path_count = 0
            for neighbor in adj_list[node]:
                path_count += dfs(neighbor)
                path_count %= MOD

            dp[node] = path_count
            return dp[node]

        return dfs(1)