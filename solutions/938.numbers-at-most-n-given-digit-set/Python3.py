class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        K = len(s)
        dp = [0] * K + [1]
        
        for i in range(K - 1, -1, -1):
            for d in digits:
                if d < s[i]:
                    dp[i] += len(digits) ** (K - i - 1)
                elif d == s[i]:
                    dp[i] += dp[i + 1]
        
        return dp[0] + sum(len(digits) ** i for i in range(1, K))