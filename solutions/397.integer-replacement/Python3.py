class Solution:
    def integerReplacement(self, n: int) -> int:
        def helper(n, memo):
            if n == 1:
                return 0
            if n in memo:
                return memo[n]
            
            if n % 2 == 0:
                memo[n] = 1 + helper(n // 2, memo)
            else:
                memo[n] = 1 + min(helper(n + 1, memo), helper(n - 1, memo))
            return memo[n]

        return helper(n, {})