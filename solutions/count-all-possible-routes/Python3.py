from typing import List

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10**9 + 7
        n = len(locations)
        
        # Initialize DP table
        dp = [[0] * (fuel + 1) for _ in range(n)]
        dp[start][fuel] = 1
        
        # Fill the DP table
        for f in range(fuel, -1, -1):
            for i in range(n):
                if dp[i][f] > 0:
                    for j in range(n):
                        if i != j:
                            cost = abs(locations[i] - locations[j])
                            if f >= cost:
                                dp[j][f - cost] = (dp[j][f - cost] + dp[i][f]) % MOD
        
        # Sum up all ways to reach the finish city with any amount of fuel
        result = sum(dp[finish][f] for f in range(fuel + 1)) % MOD
        return result