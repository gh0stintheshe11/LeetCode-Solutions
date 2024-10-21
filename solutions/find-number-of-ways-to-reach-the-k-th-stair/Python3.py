class Solution:
    def __init__(self):
        self.dp = {}
    
    def solve(self, k, i, jup, flag):
        if k + 5 <= i:
            return 0
        if jup > 31:
            return 0

        if i in self.dp and self.dp[i][jup][flag] != -1:
            return self.dp[i][jup][flag]

        res = 1 if k == i else 0

        if flag:
            res += self.solve(k, i - 1, jup, 0)
        if i + (1 << jup) <= k + 1:
            res += self.solve(k, i + (1 << jup), jup + 1, 1)

        if i not in self.dp:
            self.dp[i] = [[-1] * 2 for _ in range(32)]

        self.dp[i][jup][flag] = res
        return res

    def waysToReachStair(self, k: int) -> int:
        return self.solve(k, 1, 0, 1)