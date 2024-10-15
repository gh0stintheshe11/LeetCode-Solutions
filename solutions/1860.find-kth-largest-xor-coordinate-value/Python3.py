from typing import List
import heapq

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        xor_matrix = [[0] * n for _ in range(m)]
        heap = []
        
        for i in range(m):
            for j in range(n):
                xor_value = matrix[i][j]
                if i > 0:
                    xor_value ^= xor_matrix[i-1][j]
                if j > 0:
                    xor_value ^= xor_matrix[i][j-1]
                if i > 0 and j > 0:
                    xor_value ^= xor_matrix[i-1][j-1]
                xor_matrix[i][j] = xor_value
                heapq.heappush(heap, xor_value)
                if len(heap) > k:
                    heapq.heappop(heap)
        
        return heap[0]