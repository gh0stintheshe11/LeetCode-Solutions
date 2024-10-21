class Solution:
    def encode(self, s: str) -> str:
        n = len(s)
        dp = [["" for _ in range(n)] for _ in range(n)]

        for l in range(n):
            for i in range(n - l):
                j = i + l
                substr = s[i:j+1]
                dp[i][j] = substr
                
                for k in range(i, j):
                    if len(dp[i][j]) > len(dp[i][k] + dp[k + 1][j]):
                        dp[i][j] = dp[i][k] + dp[k + 1][j]
                
                for k in range(1, len(substr)):
                    repeat_str = substr[:k]
                    if repeat_str and substr == repeat_str * (len(substr) // len(repeat_str)):
                        encoded_str = f"{len(substr) // len(repeat_str)}[{dp[i][i + k - 1]}]"
                        if len(encoded_str) < len(dp[i][j]):
                            dp[i][j] = encoded_str
        
        return dp[0][n-1]