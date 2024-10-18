from typing import List

class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        # This will hold the length of the alternating subarray ending at position `i`
        dp = 1

        for i in range(n):
            # If it's the first element, it's an alternating subarray itself
            if i == 0:
                dp = 1
            else:
                # Check if the current element is different from the previous one
                if nums[i] != nums[i - 1]:
                    dp += 1
                else:
                    dp = 1
            count += dp
        return count