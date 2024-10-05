class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [1] + [0]*len(t)
        for i in range(1, len(s)+1):
            for j in range(len(t), 0, -1):
                if s[i-1] == t[j-1]:
                    dp[j] += dp[j-1]
        return dp[-1]