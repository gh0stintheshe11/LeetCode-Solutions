from typing import List

class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        n, k = len(flights), len(days[0])
        dp = [[-1] * n for _ in range(k)]
        dp[0][0] = days[0][0]
        
        for j in range(1, n):
            if flights[0][j] == 1:
                dp[0][j] = days[j][0]
        
        for week in range(1, k):
            for city in range(n):
                if dp[week-1][city] == -1:
                    continue
                for dest in range(n):
                    if (city == dest or flights[city][dest] == 1) and dp[week-1][city] != -1:
                        dp[week][dest] = max(dp[week][dest], dp[week-1][city] + days[dest][week])
        
        return max(dp[-1])

# Define the input example 1
flights = [[0,1,1],[1,0,1],[1,1,0]]
days = [[1,3,1],[6,0,3],[3,3,3]]
solution = Solution()
print(solution.maxVacationDays(flights, days))  # Output: 12