class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        max_val = 0
        n = len(arr1)
        for sign1 in [-1, 1]:
            for sign2 in [-1, 1]:
                max_expr = float('-inf')
                min_expr = float('inf')
                for i in range(n):
                    expr = sign1 * arr1[i] + sign2 * arr2[i] + i
                    max_expr = max(max_expr, expr)
                    min_expr = min(min_expr, expr)
                max_val = max(max_val, max_expr - min_expr)
        return max_val