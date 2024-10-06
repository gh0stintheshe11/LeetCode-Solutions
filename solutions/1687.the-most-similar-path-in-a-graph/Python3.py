class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        from collections import defaultdict
        import heapq

        # Build graph
        graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)

        m = len(targetPath)
        # DP table: dp[i][j] = minimum edit distance for targetPath up to i using city j
        dp = [[float('inf')] * n for _ in range(m)]
        prev = [[-1] * n for _ in range(m)]

        # Initial population
        for node in range(n):
            dp[0][node] = (names[node] != targetPath[0])

        # Fill dp table
        for i in range(1, m):
            for j in range(n):
                for neighbor in graph[j]:
                    edit_distance = dp[i - 1][neighbor] + (names[j] != targetPath[i])
                    if edit_distance < dp[i][j]:
                        dp[i][j] = edit_distance
                        prev[i][j] = neighbor

        # Get minimum edit distance at the end of the path and its last node
        min_distance, last_node = min((dp[m - 1][node], node) for node in range(n))

        # Reconstruct path
        path = [last_node]
        for i in range(m - 1, 0, -1):
            last_node = prev[i][last_node]
            path.append(last_node)

        return path[::-1]