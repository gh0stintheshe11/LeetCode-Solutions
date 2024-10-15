class Solution:
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (maxLength + 1)
        dp[0] = 1

        for i in range(1, maxLength + 1):
            if i >= oneGroup:
                dp[i] = (dp[i] + dp[i - oneGroup]) % MOD
            if i >= zeroGroup:
                dp[i] = (dp[i] + dp[i - zeroGroup]) % MOD

        result = sum(dp[minLength:maxLength + 1]) % MOD
        return result