class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = [-1] * n  # -1 indicates unvisited
        longest_cycle_length = -1

        def dfs(node, path_visited, step):
            nonlocal longest_cycle_length
            if node == -1:
                return
            if visited[node] >= 0:
                if node in path_visited:
                    cycle_length = step - path_visited[node]
                    longest_cycle_length = max(longest_cycle_length, cycle_length)
                return
            
            path_visited[node] = step
            visited[node] = step
            dfs(edges[node], path_visited, step + 1)
            path_visited.pop(node, None)

        for start_node in range(n):
            if visited[start_node] == -1:
                dfs(start_node, {}, 0)

        return longest_cycle_length