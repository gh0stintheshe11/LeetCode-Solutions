from typing import List
from collections import defaultdict, Counter

class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        def count_subarrays_with_max_uniqueness(target: int) -> int:
            count = 0
            left = 0
            freq = defaultdict(int)
            unique_count = 0

            for right in range(len(nums)):
                freq[nums[right]] += 1
                if freq[nums[right]] == 1:
                    unique_count += 1

                while unique_count > target:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        unique_count -= 1
                    left += 1
                
                count += (right - left + 1)
            return count

        total_subarrays = len(nums) * (len(nums) + 1) // 2
        median_position = (total_subarrays + 1) // 2

        low, high = 1, len(nums)
        while low < high:
            mid = (low + high) // 2
            if count_subarrays_with_max_uniqueness(mid) < median_position:
                low = mid + 1
            else:
                high = mid
                
        return low