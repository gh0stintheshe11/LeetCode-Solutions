from typing import List

class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        ones_indices = [i for i, num in enumerate(nums) if num == 1]
        
        pre_sums = [0] * (len(ones_indices) + 1)
        for i in range(len(ones_indices)):
            pre_sums[i + 1] = pre_sums[i] + ones_indices[i]

        result = float('inf')
        for i in range(len(ones_indices) - k + 1):
            mid = i + k // 2
            right = pre_sums[i + k] - pre_sums[mid + 1]
            left = pre_sums[mid] - pre_sums[i]
            mid_val = ones_indices[mid]

            left_cost = mid_val * (mid - i) - left
            right_cost = right - mid_val * ((i + k) - mid - 1)

            result = min(result, left_cost + right_cost)

        adjustments = (k // 2) * ((k + 1) // 2)
        return result - adjustments