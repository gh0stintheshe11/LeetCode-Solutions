from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) > 6 * len(nums2) or len(nums2) > 6 * len(nums1):
            return -1
        
        sum1, sum2 = sum(nums1), sum(nums2)
        
        if sum1 < sum2:
            nums1, nums2 = nums2, nums1
            sum1, sum2 = sum2, sum1
        
        diff = sum1 - sum2
        count = 0
        
        possible_changes = []
        
        for num in nums1:
            if num > 1:
                possible_changes.append(num - 1)
        
        for num in nums2:
            if num < 6:
                possible_changes.append(6 - num)
        
        possible_changes.sort(reverse=True)
        
        for change in possible_changes:
            if diff <= 0:
                break
            diff -= change
            count += 1
        
        return count if diff <= 0 else -1