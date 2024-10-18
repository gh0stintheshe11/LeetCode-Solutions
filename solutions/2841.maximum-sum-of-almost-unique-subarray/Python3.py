from typing import List
from collections import defaultdict

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        n = len(nums)
        if n < k:
            return 0

        window_sum = 0
        max_sum = 0
        count_map = defaultdict(int)
        distinct_count = 0
        left = 0

        for right in range(n):
            window_sum += nums[right]
            count_map[nums[right]] += 1
            if count_map[nums[right]] == 1:
                distinct_count += 1

            if right - left + 1 == k:
                if distinct_count >= m:
                    max_sum = max(max_sum, window_sum)
                
                window_sum -= nums[left]
                count_map[nums[left]] -= 1
                if count_map[nums[left]] == 0:
                    distinct_count -= 1
                left += 1

        return max_sum