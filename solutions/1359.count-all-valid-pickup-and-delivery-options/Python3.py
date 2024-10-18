class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        count = 1
        for i in range(1, n + 1):
            count *= i * (2 * i - 1)
            count %= MOD
        return count