from typing import List

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        max_length = 0
        l = 0

        while l < n:
            if nums[l] % 2 == 0 and nums[l] <= threshold:
                r = l
                while r < n and nums[r] <= threshold and (r == l or nums[r] % 2 != nums[r - 1] % 2):
                    r += 1
                max_length = max(max_length, r - l)
                l = r
            else:
                l += 1
        
        return max_length