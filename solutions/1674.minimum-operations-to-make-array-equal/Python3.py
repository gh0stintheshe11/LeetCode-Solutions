class Solution:
    def minOperations(self, n: int) -> int:
        return (n // 2) * (n // 2 + n % 2)