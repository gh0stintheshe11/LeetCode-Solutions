from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # Sort the numbers
        nums.sort()
        n = len(nums)
        
        # Initialize the best product as the smallest element if it's the only positive or only negative
        best_product = nums[-1]
        
        # Start product calculation
        product = 1
        used_elem = False
        
        # Iterate over the numbers, trying to use them in pairs
        for i in range(n):
            if nums[i] > 0:
                product *= nums[i]
                used_elem = True
        
        # If there's an even number of negative numbers, use them all
        # If there's an odd count, use up to the second last one
        neg_count = len([num for num in nums if num < 0])
        if neg_count % 2 == 1:
            neg_count -= 1
        
        for i in range(neg_count):
            product *= nums[i]
            used_elem = True

        return product if used_elem else nums[-1]