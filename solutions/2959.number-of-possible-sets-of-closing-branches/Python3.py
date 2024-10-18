class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        ans = 0
        for m in range(1<<n): 
            dist = [[float('inf')]*n for _ in range(n)]
            for u in range(n): 
                if m & 1<<u: dist[u][u] = 0 
            for u, v, w in roads: 
                if m & 1<<u and m & 1<<v: 
                    dist[u][v] = dist[v][u] = min(dist[v][u], w) 
            for k in range(n): 
                for u in range(n): 
                    for v in range(n): 
                        dist[u][v] = min(dist[u][v], dist[u][k] + dist[k][v])
            for u in range(n): 
                if m & 1<<u: 
                    for v in range(n): 
                        if m & 1<<v and dist[u][v] > maxDistance: break 
                    else: continue 
                    break 
            else: ans += 1
        return ans