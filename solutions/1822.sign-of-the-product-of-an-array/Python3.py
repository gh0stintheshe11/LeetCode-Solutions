from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # Check if there is any zero in the array
        for num in nums:
            if num == 0:
                return 0
        
        # Count the number of negative numbers
        negative_count = 0
        for num in nums:
            if num < 0:
                negative_count += 1
        
        # If the count of negative numbers is odd, the product is negative
        if negative_count % 2 == 1:
            return -1
        else:
            return 1
