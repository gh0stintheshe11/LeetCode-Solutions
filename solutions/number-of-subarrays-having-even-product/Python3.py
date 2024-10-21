from typing import List

class Solution:
    def evenProduct(self, nums: List[int]) -> int:
        count = 0
        last_even_index = -1
        n = len(nums)
        
        for i in range(n):
            if nums[i] % 2 == 0:
                last_even_index = i
            count += last_even_index + 1
        
        return count