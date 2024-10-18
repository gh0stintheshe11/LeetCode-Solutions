from typing import List

class Solution:
    def minArrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        if 0 in nums:  
            return 1
        
        i = 0
        min_length = n
        
        while i < n:
            j = i + 1
            product = nums[i]
            while j < n:
                if product * nums[j] > k:
                    break
                product *= nums[j]
                j += 1
            min_length -= (j - i - 1)
            i = j
        
        return min_length