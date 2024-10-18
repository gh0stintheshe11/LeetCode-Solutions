from typing import List

class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        n = len(nums)
        num_strs = [str(num) for num in nums]
        num_digits = len(num_strs[0])
        
        total_diff_sum = 0
        
        for pos in range(num_digits):
            count = [0] * 10
            for num_str in num_strs:
                digit = int(num_str[pos])
                count[digit] += 1
            
            total_pairs = 0
            for digit in range(10):
                total_pairs += count[digit] * (n - count[digit])
            
            total_diff_sum += total_pairs
        
        return total_diff_sum // 2