from typing import List
from collections import defaultdict

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count_map = defaultdict(int)
        current_pairs = 0
        result = 0
        l = 0

        for r in range(n):
            current_number = nums[r]
            # Increase the count of pairs by the number of occurrences of current_number
            current_pairs += count_map[current_number]
            # Add this number to the count_map
            count_map[current_number] += 1

            # Check if we have at least k pairs
            while current_pairs >= k:
                # If the current subarray [l, r] is good, all subarrays starting from l to r are good
                result += n - r
                # Try to shrink the window from the left
                current_pairs -= count_map[nums[l]] - 1
                count_map[nums[l]] -= 1
                l += 1
        
        return result