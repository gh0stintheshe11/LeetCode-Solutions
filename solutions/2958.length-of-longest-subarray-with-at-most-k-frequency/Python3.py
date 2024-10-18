from typing import List
from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(len(nums)):
            count[nums[right]] += 1

            while count[nums[right]] > k:
                count[nums[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len