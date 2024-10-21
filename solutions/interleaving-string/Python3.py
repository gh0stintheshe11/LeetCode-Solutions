class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1) + 1, len(s2) + 1, len(s3) + 1
        if l1 + l2 - 1 != l3: return False
        dp = [[True] * l2 for _ in range(l1)]
        for i in range(1, l1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, l2):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, l1):
            for j in range(1, l2):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
        return dp[-1][-1]