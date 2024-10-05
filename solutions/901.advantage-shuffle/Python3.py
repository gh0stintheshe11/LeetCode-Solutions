from typing import List
from collections import deque

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        sorted_indices = sorted(range(len(nums2)), key=lambda i: nums2[i])
        sorted_nums2 = sorted(nums2)
        
        answer = [0] * len(nums2)
        remaining = []
        
        j = 0
        for num in nums1:
            if num > sorted_nums2[j]:
                answer[sorted_indices[j]] = num
                j += 1
            else:
                remaining.append(num)
        
        for i in range(j, len(nums2)):
            answer[sorted_indices[i]] = remaining.pop(0)
        
        return answer