from collections import Counter
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        
        # Split nums into odd and even indices
        odd_counts = Counter(nums[i] for i in range(1, len(nums), 2))
        even_counts = Counter(nums[i] for i in range(0, len(nums), 2))
        
        # Get the most common elements and their counts
        odd_most_common = odd_counts.most_common(2) + [(0, 0), (0, 0)]
        even_most_common = even_counts.most_common(2) + [(0, 0), (0, 0)]

        _, odd_freq_1 = odd_most_common[0]
        odd_elem_1 = odd_most_common[0][0]
        _, odd_freq_2 = odd_most_common[1]

        _, even_freq_1 = even_most_common[0]
        even_elem_1 = even_most_common[0][0]
        _, even_freq_2 = even_most_common[1]
        
        n = len(nums)
        
        if odd_elem_1 != even_elem_1:
            # If the most common elements are not the same, use them
            return n - odd_freq_1 - even_freq_1
        else:
            # Otherwise, choose the best alternative combination
            return min(n - odd_freq_2 - even_freq_1, n - odd_freq_1 - even_freq_2)