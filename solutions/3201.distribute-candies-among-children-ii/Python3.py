class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        total_ways = 0
        for i in range(min(n, limit) + 1):
            max_j = min(limit, n - i)
            min_j = max(0, n - i - limit)
            total_ways += max(0, max_j - min_j + 1)
        return total_ways