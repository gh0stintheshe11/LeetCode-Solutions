from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        prefix = [float('inf')] * n
        suffix = [float('inf')] * n
        min_length = float('inf')
        
        # Calculate prefix min lengths
        sum_map = {0: -1}
        current_sum = 0
        for i in range(n):
            current_sum += arr[i]
            if current_sum - target in sum_map:
                length = i - sum_map[current_sum - target]
                min_length = min(min_length, length)
            prefix[i] = min_length
            sum_map[current_sum] = i
        
        min_length = float('inf')
        sum_map = {0: n}
        current_sum = 0
        for i in range(n-1, -1, -1):
            current_sum += arr[i]
            if current_sum - target in sum_map:
                length = sum_map[current_sum - target] - i
                min_length = min(min_length, length)
            suffix[i] = min_length
            sum_map[current_sum] = i
        
        # Calculate the minimum sum of lengths using prefix and suffix arrays
        min_total_length = float('inf')
        for i in range(n - 1):
            if prefix[i] < float('inf') and suffix[i + 1] < float('inf'):
                min_total_length = min(min_total_length, prefix[i] + suffix[i + 1])
        
        return min_total_length if min_total_length < float('inf') else -1