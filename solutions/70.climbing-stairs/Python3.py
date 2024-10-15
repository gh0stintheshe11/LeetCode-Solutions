class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        a = 1
        b = 2
        for _ in range(2, n):
            tmp = b
            b = a + b
            a = tmp
        return b