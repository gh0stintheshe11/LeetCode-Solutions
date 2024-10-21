class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.MAX_LOG = 16  # At most 2^16 = 65536 > 5 * 10^4
        self.dp = [[-1] * (self.MAX_LOG) for _ in range(n)]
        
        # Initialize the first ancestor
        for i in range(n):
            self.dp[i][0] = parent[i]
        
        # DP table filling
        for j in range(1, self.MAX_LOG):
            for i in range(n):
                if self.dp[i][j - 1] != -1:
                    self.dp[i][j] = self.dp[self.dp[i][j - 1]][j - 1]
                else:
                    self.dp[i][j] = -1

    def getKthAncestor(self, node: int, k: int) -> int:
        current = node
        for i in range(self.MAX_LOG):
            if k & (1 << i):
                current = self.dp[current][i]
                if current == -1:
                    break
        return current