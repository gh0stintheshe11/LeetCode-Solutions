class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        def dfs(node):
            for x in map(str, range(k)):
                neighbor = node + x
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor[1:])
                    result.append(x)
        
        start = '0' * (n - 1)
        visited = set()
        result = []
        dfs(start)
        return ''.join(result) + start