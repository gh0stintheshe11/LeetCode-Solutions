from typing import List

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def can_detonate(from_bomb, to_bomb):
            x1, y1, r1 = bombs[from_bomb]
            x2, y2, _ = bombs[to_bomb]
            return (x2 - x1) ** 2 + (y2 - y1) ** 2 <= r1 ** 2
        
        def dfs(bomb_index, visited):
            stack = [bomb_index]
            count = 0
            while stack:
                current = stack.pop()
                if not visited[current]:
                    visited[current] = True
                    count += 1
                    for next_bomb in graph[current]:
                        if not visited[next_bomb]:
                            stack.append(next_bomb)
            return count
        
        n = len(bombs)
        graph = [[] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if i != j and can_detonate(i, j):
                    graph[i].append(j)
        
        max_detonations = 0
        for i in range(n):
            visited = [False] * n
            max_detonations = max(max_detonations, dfs(i, visited))
        
        return max_detonations