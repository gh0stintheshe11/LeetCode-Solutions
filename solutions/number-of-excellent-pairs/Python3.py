from typing import List
from collections import Counter

class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        # Helper function to count set bits in a number
        def count_bits(x):
            return bin(x).count('1')

        # Use a set to remove duplicates and count set bits for each unique number
        unique_nums = set(nums)
        bit_counts = [count_bits(num) for num in unique_nums]

        # Count the occurrences of each bit count
        count = Counter(bit_counts)
        
        # To find pairs (i, j) such that bit_counts[i] + bit_counts[j] >= k
        excellent_pairs = 0
        for bi in count:
            for bj in count:
                if bi + bj >= k:
                    excellent_pairs += count[bi] * count[bj]

        return excellent_pairs