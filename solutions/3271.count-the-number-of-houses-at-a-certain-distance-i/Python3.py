from typing import List
from collections import deque

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        result = [0] * n
        
        def bfs(start):
            # Helper function to perform BFS and compute distances from start
            distances = [float('inf')] * (n + 1)
            q = deque([start])
            distances[start] = 0
            
            while q:
                cur = q.popleft()
                for neighbor in (cur - 1, cur + 1):
                    if 1 <= neighbor <= n and distances[neighbor] == float('inf'):
                        distances[neighbor] = distances[cur] + 1
                        q.append(neighbor)
                # Consider the additional street from x to y
                if cur == x and distances[y] == float('inf'):
                    distances[y] = distances[cur] + 1
                    q.append(y)
                elif cur == y and distances[x] == float('inf'):
                    distances[x] = distances[cur] + 1
                    q.append(x)

            return distances

        # Calculate all-pairs shortest paths using BFS from each node
        for i in range(1, n + 1):
            dist = bfs(i)
            for j in range(1, n + 1):
                if i != j:
                    k = dist[j]
                    result[k - 1] += 1
        
        return result