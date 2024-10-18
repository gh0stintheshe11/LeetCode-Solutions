from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        dp = {}
        
        for i in range(len(arr)):
            dp[arr[i]] = 1  # Each element itself can form a tree
            for j in range(i):
                if arr[i] % arr[j] == 0:  # arr[j] should be a factor of arr[i]
                    right = arr[i] // arr[j]
                    if right in dp:
                        dp[arr[i]] += dp[arr[j]] * dp[right]
                        dp[arr[i]] %= MOD
        
        return sum(dp.values()) % MOD