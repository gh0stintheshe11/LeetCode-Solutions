class Solution:
    def minimumCost(self, sentence, k):
        @lru_cache(None)
        def dfs(i):
            if i+k >= len(sentence): return 0

            min_val = float("inf")

            for j in range(i, i+k+1):
                if sentence[j] == " ":
                    min_val = min(min_val, (k+i-j)**2 + dfs(j+1))

            return min_val

        return dfs(0)