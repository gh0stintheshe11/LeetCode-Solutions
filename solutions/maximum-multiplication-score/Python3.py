class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        memo = {}
        def dfs(i, j):
            if i == len(a):
                return 0
            if j == len(b):
                return float('-inf')
            if (i, j) in memo:
                return memo[(i, j)]
            take_dis = a[i] * b[j] + dfs(i + 1, j + 1)
            not_take = dfs(i, j + 1)
            memo[(i, j)] = max(take_dis, not_take)
            return memo[(i, j)]
        
        return dfs(0, 0)