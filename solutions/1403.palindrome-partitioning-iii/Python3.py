class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        
        def min_convert_to_palindrome(start: int, end: int) -> int:
            changes = 0
            while start < end:
                if s[start] != s[end]:
                    changes += 1
                start += 1
                end -= 1
            return changes
        
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                cost[i][j] = min_convert_to_palindrome(i, j)
        
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        
        for i in range(1, n + 1):
            for j in range(1, min(k, i) + 1):
                for m in range(j - 1, i):
                    dp[i][j] = min(dp[i][j], dp[m][j - 1] + cost[m][i - 1])
        
        return dp[n][k]