class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        MOD = 10**9 + 7
        n = len(s)

        def isPrime(c):
            return c in {'2', '3', '5', '7'}

        # If the first character is not prime or the last character is prime, return 0
        if not isPrime(s[0]) or isPrime(s[-1]):
            return 0

        # Initialize DP table
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for j in range(1, k + 1):
            prefix_sum = 0
            for i in range(minLength, n + 1):
                if i - minLength >= 0 and not isPrime(s[i-minLength-1]) and isPrime(s[i-minLength]):
                    prefix_sum = (prefix_sum + dp[i-minLength][j-1]) % MOD
                if not isPrime(s[i-1]) and (i == n or isPrime(s[i])):
                    dp[i][j] = prefix_sum

        return dp[n][k]