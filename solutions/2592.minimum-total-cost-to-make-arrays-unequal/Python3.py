from typing import List
import collections

class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0 
        base_frequency = collections.defaultdict(int)
        total = 0 
        most_frequent = 0 
        max_frequency = 0 
        for index, (num1, num2) in enumerate(zip(nums1, nums2)) : 
            if num1 == num2 : 
                result += index 
                total += 1 
                base_frequency[num1] += 1 
                if base_frequency[num1] > max_frequency : 
                    max_frequency = base_frequency[num1]
                    most_frequent = num1 
        if 2 * max_frequency <= total : 
            return result 
        remainder = 2 * max_frequency - total 
        for index, (num1, num2) in enumerate(zip(nums1, nums2)) : 
            if num1 != num2 and num1 != most_frequent and num2 != most_frequent : 
                result += index 
                remainder -= 1 
            if remainder == 0 : 
                return result 
        return -1