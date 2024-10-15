from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Count the occurrences of each element in nums1
        count_nums1 = Counter(nums1)
        
        # Initialize the result list
        result = []
        
        # Iterate through nums2
        for num in nums2:
            # If the element is in count_nums1 and the count is greater than 0
            if count_nums1[num] > 0:
                # Add the element to the result list
                result.append(num)
                # Decrement the count in the dictionary
                count_nums1[num] -= 1
        
        return result