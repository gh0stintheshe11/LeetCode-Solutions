class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:

        n1, n2 = len(s1)+1, len(s2)+1
        i1, i2, ans = n1-1, n2-1, ''
        s1, s2 = s1.rjust(n1), s2.rjust(n2)
        dp = [[0] * n2 for _ in range(n1)]

        for i1 in range(1, n1):
            for i2 in range(1, n2):
                if s1[i1] == s2[i2]:
                    dp[i1][i2] = dp[i1-1][i2-1] + 1
                else:
                    dp[i1][i2] = max(dp[i1 - 1][i2], dp[i1][i2-1])

        while i1 | i2:
            if not i1 * i2:
                ans += s1[i1] if i1 else s2[i2]
                i2 -= bool(i2)
                i1 -= bool(i1)
            elif s1[i1] == s2[i2]:
                ans += s1[i1]
                i1 -= 1
                i2 -= 1
            elif dp[i1][i2] == dp[i1-1][i2]:
                ans += s1[i1]
                i1 -= 1
            else:
                ans += s2[i2]
                i2 -= 1

        return ans[::-1]