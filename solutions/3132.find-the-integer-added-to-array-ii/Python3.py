from typing import List

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        min2 = min(nums2)
        result = float('inf')

        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                remaining_nums1 = [nums1[k] for k in range(len(nums1)) if k != i and k != j]
                min1 = min(remaining_nums1)
                x = min2 - min1
                possible_nums1 = sorted([num + x for num in remaining_nums1])
                
                if possible_nums1 == sorted(nums2):
                    result = min(result, x)
        
        return result