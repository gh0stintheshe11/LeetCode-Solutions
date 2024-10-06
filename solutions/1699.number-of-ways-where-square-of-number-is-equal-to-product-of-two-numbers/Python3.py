from typing import List
from collections import Counter

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def countPairs(nums: List[int], targetSquare: int) -> int:
            count = 0
            freq = Counter(nums)
            for num in freq:
                if targetSquare % num == 0:
                    complement = targetSquare // num
                    if complement in freq:
                        if num == complement:
                            count += freq[num] * (freq[num] - 1) // 2
                        elif num < complement:
                            count += freq[num] * freq[complement]
            return count
        
        result = 0
        for n in nums1:
            result += countPairs(nums2, n * n)
        for n in nums2:
            result += countPairs(nums1, n * n)
        
        return result