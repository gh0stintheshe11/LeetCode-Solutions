from typing import List

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0]
        
        max_ending_here = arr[0]
        max_so_far = arr[0]
        max_ending_here_with_deletion = 0
        max_sum_with_deletion = float('-inf')

        for i in range(1, n):
            max_ending_here_with_deletion = max(max_ending_here, max_ending_here_with_deletion + arr[i])
            max_sum_with_deletion = max(max_sum_with_deletion, max_ending_here_with_deletion)
            max_ending_here = max(max_ending_here + arr[i], arr[i])
            max_so_far = max(max_so_far, max_ending_here)

        return max(max_so_far, max_sum_with_deletion)