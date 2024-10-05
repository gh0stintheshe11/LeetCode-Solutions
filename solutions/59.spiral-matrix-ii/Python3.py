class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        res = [[0] * n for _ in range(n)]
        total = n*n
        num = 1
        layer = 0
        while num <= total:
            for i in range(layer, n-layer):
                res[layer][i] = num
                num += 1
            for i in range(layer+1, n-layer):
                res[i][n-layer-1] = num
                num += 1
            for i in range(layer+1, n-layer):
                res[n-layer-1][n-i-1] = num
                num += 1
            for i in range(layer+1, n-layer-1):
                res[n-i-1][layer] = num
                num += 1
            layer += 1
        return res