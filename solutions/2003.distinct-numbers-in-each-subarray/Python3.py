from typing import List
from collections import defaultdict

class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        distinct_count = []
        freq = defaultdict(int)
        
        # Initialize frequency dictionary for the first window
        for i in range(k):
            freq[nums[i]] += 1
        distinct_count.append(len(freq))
        
        # Slide the window across the array
        for i in range(k, len(nums)):
            # Remove the element that is moving out of the window
            freq[nums[i - k]] -= 1
            if freq[nums[i - k]] == 0:
                del freq[nums[i - k]]
            # Add the new element of the window
            freq[nums[i]] += 1
            # Add the number of distinct elements to the result
            distinct_count.append(len(freq))
        
        return distinct_count