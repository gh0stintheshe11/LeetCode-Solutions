from typing import List

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        def is_strictly_increasing(a):
            return all(a[i] < a[i+1] for i in range(len(a) - 1))

        total_count = 0
        n = len(nums)

        for start in range(n):
            for end in range(start, n):
                subarray = nums[start:end + 1]
                remaining = nums[:start] + nums[end + 1:]
                if is_strictly_increasing(remaining):
                    total_count += 1

        return total_count