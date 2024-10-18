class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        total_cost = 0

        for i in range(1, n):
            if s[i] != s[i - 1]:
                total_cost += min(i, n - i)

        return total_cost