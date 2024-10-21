from typing import List
import bisect

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        def max_sum_no_larger_than_k(nums, k):
            curr_sum, max_sum = 0, float('-inf')
            prefix_sums = [0]
            for num in nums:
                curr_sum += num
                idx = bisect.bisect_left(prefix_sums, curr_sum - k)
                if idx < len(prefix_sums):
                    max_sum = max(max_sum, curr_sum - prefix_sums[idx])
                bisect.insort(prefix_sums, curr_sum)
            return max_sum
        
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        max_sum = float('-inf')
        
        for left in range(n):
            row_sums = [0] * m
            for right in range(left, n):
                for row in range(m):
                    row_sums[row] += matrix[row][right]
                max_sum = max(max_sum, max_sum_no_larger_than_k(row_sums, k))
        
        return max_sum