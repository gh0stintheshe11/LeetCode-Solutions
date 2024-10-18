class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        from collections import defaultdict
        
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        def dfs(node, parent):
            total_time = 0
            for neighbor in tree[node]:
                if neighbor == parent:
                    continue
                time_to_collect = dfs(neighbor, node)
                if time_to_collect > 0 or hasApple[neighbor]:
                    total_time += time_to_collect + 2
            return total_time
        
        return dfs(0, -1)