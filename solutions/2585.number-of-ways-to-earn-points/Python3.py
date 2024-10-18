from typing import List

class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        MOD = 10**9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for count, marks in types:
            new_dp = dp[:]
            for current_target in range(marks, target + 1):
                for solved in range(1, count + 1):
                    score = solved * marks
                    if score > current_target:
                        break
                    new_dp[current_target] = (new_dp[current_target] + dp[current_target - score]) % MOD
            dp = new_dp
        
        return dp[target]