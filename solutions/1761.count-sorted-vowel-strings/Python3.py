class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[0] * 5 for _ in range(n + 1)]
        
        for i in range(5):
            dp[1][i] = 1
        
        for length in range(2, n + 1):
            for vowel in range(5):
                dp[length][vowel] = sum(dp[length-1][:vowel+1])
        
        return sum(dp[n])