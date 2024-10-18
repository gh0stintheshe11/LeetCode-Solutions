from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        # Ensure min_index is smaller for easier processing
        if min_index > max_index:
            min_index, max_index = max_index, min_index

        # Option 1: Remove both elements from the front
        option1 = max_index + 1
        
        # Option 2: Remove both elements from the back
        option2 = n - min_index
        
        # Option 3: Remove one from the front, the other from the back
        option3 = min_index + 1 + n - max_index

        return min(option1, option2, option3)