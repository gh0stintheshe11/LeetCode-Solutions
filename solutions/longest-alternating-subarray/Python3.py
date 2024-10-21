from typing import List

class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        max_length = 0
        n = len(nums)
        current_length = 0

        for i in range(1, n):
            if nums[i] - nums[i - 1] == 1:
                current_length = 2
                pattern = 1
                for j in range(i + 1, n):
                    expected_diff = -1 if pattern == 1 else 1
                    if nums[j] - nums[j - 1] == expected_diff:
                        current_length += 1
                        pattern *= -1
                    else:
                        break
                max_length = max(max_length, current_length)

        return max_length if max_length > 0 else -1