from typing import List

class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        max_num = max(nums)
        
        # Frequency array for numbers in nums
        freq = [0] * (max_num + 1)
        for num in nums:
            freq[num] += 1
        
        # Prefix sum of frequencies to calculate range sums efficiently
        prefix_sum = [0] * (max_num + 1)
        for i in range(1, max_num + 1):
            prefix_sum[i] = prefix_sum[i - 1] + freq[i]

        result = 0

        # For each number, calculate its contribution to the result
        for i in range(1, max_num + 1):
            if freq[i] > 0:
                multiple = 1
                while i * multiple <= max_num:
                    # Determine the range of indices for current multiple
                    left = i * multiple
                    right = min(max_num, i * (multiple + 1) - 1)
                    
                    # Calculate the floored sum contributions
                    sum_contribution = (prefix_sum[right] - prefix_sum[left - 1]) * multiple * freq[i]
                    result = (result + sum_contribution) % MOD
                    
                    multiple += 1

        return result