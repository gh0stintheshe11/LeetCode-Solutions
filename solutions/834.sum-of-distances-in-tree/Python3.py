class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Initialize count and answer array
        count = [1] * n
        answer = [0] * n

        # Helper function to perform DFS and calculate initial distances and count of nodes
        def dfs1(node, parent):
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs1(neighbor, node)
                    count[node] += count[neighbor]
                    answer[node] += answer[neighbor] + count[neighbor]
        
        # Second DFS to calculate the final distances based on subtree info
        def dfs2(node, parent):
            for neighbor in graph[node]:
                if neighbor != parent:
                    answer[neighbor] = answer[node] - count[neighbor] + (n - count[neighbor])
                    dfs2(neighbor, node)
        
        dfs1(0, -1)
        dfs2(0, -1)
        
        return answer