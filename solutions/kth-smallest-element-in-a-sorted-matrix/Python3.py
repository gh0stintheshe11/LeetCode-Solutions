from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import heapq
        n = len(matrix)
        min_heap = []
        for r in range(n):
            heapq.heappush(min_heap, (matrix[r][0], r, 0))

        element = 0
        for _ in range(k):
            element, r, c = heapq.heappop(min_heap)
            if c < n - 1:
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))

        return element