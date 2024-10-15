class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return k
        same = k
        diff = k * (k - 1)
        for i in range(3, n + 1):
            same, diff = diff, (same + diff) * (k - 1)
        return same + diff