from typing import List

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def triangleArea(A, B, C):
            return abs(A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1])) / 2

        n = len(points)
        max_area = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    max_area = max(max_area, triangleArea(points[i], points[j], points[k]))
        
        return max_area