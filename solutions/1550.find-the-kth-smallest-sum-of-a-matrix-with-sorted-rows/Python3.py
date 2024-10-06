from heapq import heappop, heappush
from typing import List, Tuple

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])
        
        def kthSmallestPairSum(A: List[int], B: List[int], k: int) -> List[int]:
            min_heap = []
            visited = set()
            heappush(min_heap, (A[0] + B[0], 0, 0))
            visited.add((0, 0))
            result = []

            while k > 0 and min_heap:
                sum_val, i, j = heappop(min_heap)
                result.append(sum_val)
                k -= 1

                if i + 1 < len(A) and (i + 1, j) not in visited:
                    heappush(min_heap, (A[i + 1] + B[j], i + 1, j))
                    visited.add((i + 1, j))
                
                if j + 1 < len(B) and (i, j + 1) not in visited:
                    heappush(min_heap, (A[i] + B[j + 1], i, j + 1))
                    visited.add((i, j + 1))
            
            return result

        sums = mat[0]
        for i in range(1, m):
            sums = kthSmallestPairSum(sums, mat[i], k)
            
        return sums[-1]