class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        n = len(robot)
        m = len(factory)

        dp = [[float('inf')] * (m+1) for _ in range(n+1)]
        dp[0][0] = 0

        for j in range(1, m+1):
            position_j, limit_j = factory[j-1]
            for i in range(n+1):
                dp[i][j] = dp[i][j-1] # Case when we do not assign any robot to this factory
                
                cost = 0
                for k in range(1, min(i, limit_j) + 1):
                    cost += abs(robot[i-k] - position_j)
                    dp[i][j] = min(dp[i][j], dp[i-k][j-1] + cost)

        return dp[n][m]