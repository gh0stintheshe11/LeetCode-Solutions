from typing import List

class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # Sort each cuboid's dimensions
        for cuboid in cuboids:
            cuboid.sort()
        
        # Sort the cuboids based on dimensions which makes sure
        # that when comparing a < b for any dimension a and b => one cuboid can fit in another
        cuboids.sort()
        
        n = len(cuboids)
        dp = [0] * n
        
        # The idea is same as longest increasing subsequence
        # For each cuboid, find the best stack height it can end with
        for i in range(n):
            dp[i] = cuboids[i][2]  # Assign height of current cuboid as base case
            
            for j in range(i):
                if (cuboids[j][0] <= cuboids[i][0] and
                    cuboids[j][1] <= cuboids[i][1] and
                    cuboids[j][2] <= cuboids[i][2]):
                    dp[i] = max(dp[i], dp[j] + cuboids[i][2])
        
        # The result will be the maximum height achievable with any cuboid stack
        return max(dp)