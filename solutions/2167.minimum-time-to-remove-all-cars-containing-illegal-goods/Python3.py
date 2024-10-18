class Solution:
    def minimumTime(self, s: str) -> int:
        n = len(s)
        left_cost = [0] * n
        right_cost = [0] * n

        left_cost[0] = 1 if s[0] == '1' else 0
        for i in range(1, n):
            if s[i] == '1':
                left_cost[i] = min(left_cost[i - 1] + 2, i + 1)
            else:
                left_cost[i] = left_cost[i - 1]

        right_cost[n - 1] = 1 if s[n - 1] == '1' else 0
        for i in range(n - 2, -1, -1):
            if s[i] == '1':
                right_cost[i] = min(right_cost[i + 1] + 2, n - i)
            else:
                right_cost[i] = right_cost[i + 1]

        result = min(left_cost[-1], right_cost[0])
        for i in range(1, n):
            result = min(result, left_cost[i - 1] + right_cost[i])

        return result