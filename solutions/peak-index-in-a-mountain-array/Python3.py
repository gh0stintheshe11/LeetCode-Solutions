from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                # We are in the increasing part of the mountain
                left = mid + 1
            else:
                # We are in the decreasing part of the mountain
                right = mid
        
        # At the end of the loop, left == right and it points to the peak index
        return left
