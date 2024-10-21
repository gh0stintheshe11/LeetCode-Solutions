from collections import defaultdict
from typing import List

class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        indices = defaultdict(list)
        for idx, num in enumerate(nums):
            indices[num].append(idx)

        max_len = 0
        for same_value_indices in indices.values():
            left = 0
            for right in range(len(same_value_indices)):
                # Use a sliding window to find the longest subarray at most k deletions
                while same_value_indices[right] - same_value_indices[left] - (right - left) > k:
                    left += 1
                max_len = max(max_len, right - left + 1)

        return max_len