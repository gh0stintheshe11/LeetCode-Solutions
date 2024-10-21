class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        import math
        INF = float('inf')
        
        # Memoization for minimum time for continuous laps
        min_lap_time = [INF] * (numLaps + 1)
        
        for f, r in tires:
            time = curlap = f
            for lap in range(1, numLaps + 1):
                if time >= f + changeTime:
                    break
                min_lap_time[lap] = min(min_lap_time[lap], curlap)
                curlap += time * r
                time *= r

        dp = [INF] * (numLaps + 1)
        dp[0] = 0
        
        for lap in range(1, numLaps + 1):
            for k in range(1, lap + 1):
                dp[lap] = min(dp[lap], min_lap_time[k] + dp[lap - k] + changeTime)

        return dp[numLaps] - changeTime