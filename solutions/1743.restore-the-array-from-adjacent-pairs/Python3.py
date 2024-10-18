class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        from collections import defaultdict
        
        # Create an adjacency list
        adjacency_list = defaultdict(list)
        for u, v in adjacentPairs:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
        
        # Find the start of the array, which is an element with only one neighbor
        start = None
        for key, neighbors in adjacency_list.items():
            if len(neighbors) == 1:
                start = key
                break
        
        # Restore the array using the adjacency list
        result = []
        visited = set()
        
        def dfs(node):
            if node in visited:
                return
            result.append(node)
            visited.add(node)
            for neighbor in adjacency_list[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        dfs(start)
        return result