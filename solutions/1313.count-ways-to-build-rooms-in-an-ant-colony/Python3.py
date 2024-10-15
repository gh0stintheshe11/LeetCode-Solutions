class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        from collections import defaultdict, deque
        import math
        
        MOD = 10**9 + 7
        
        n = len(prevRoom)
        tree = defaultdict(list)
        
        # Construct the tree
        for child, parent in enumerate(prevRoom):
            if parent != -1:
                tree[parent].append(child)
        
        factorials = [1] * (n + 1)
        inv_factorials = [1] * (n + 1)
        
        # Precompute factorials and inverse factorials
        for i in range(2, n + 1):
            factorials[i] = factorials[i - 1] * i % MOD
        
        def mod_inv(x, m):
            return pow(x, m - 2, m)
        
        for i in range(2, n + 1):
            inv_factorials[i] = mod_inv(factorials[i], MOD)
        
        def dfs(node):
            ways = 1
            size = 0
            for child in tree[node]:
                child_ways, child_size = dfs(child)
                ways = ways * child_ways % MOD
                ways = ways * inv_factorials[child_size] % MOD
                size += child_size
            size += 1
            ways = ways * factorials[size - 1] % MOD
            return ways, size
        
        result, _ = dfs(0)
        
        return result