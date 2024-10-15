class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        import functools
        
        size1, size2 = len(cost), len(cost[0])
        min_cost_to_connect_second_group = [min(cost[i][j] for i in range(size1)) for j in range(size2)]
        
        @functools.lru_cache(None)
        def dp(i, mask):
            if i == size1:
                return sum(min_cost_to_connect_second_group[j] for j in range(size2) if not (mask & (1 << j)))
            
            res = float('inf')
            for j in range(size2):
                res = min(res, cost[i][j] + dp(i + 1, mask | (1 << j)))
            return res
        
        return dp(0, 0)