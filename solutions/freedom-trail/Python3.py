class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        from collections import defaultdict
        
        # Build a map of character to indexes for quick lookup
        char_to_index = defaultdict(list)
        for i, ch in enumerate(ring):
            char_to_index[ch].append(i)
        
        n, m = len(ring), len(key)
        
        # Use memoization to remember the minimum steps at each state
        memo = {}
        
        def dp(i, j):
            # i is the current position in ring, j is the position in key
            if j == m:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            res = float('inf')
            for k in char_to_index[key[j]]:
                diff = abs(k - i)
                step = min(diff, n - diff)
                res = min(res, step + dp(k, j + 1))
            
            memo[(i, j)] = res + 1
            return memo[(i, j)]
        
        return dp(0, 0)