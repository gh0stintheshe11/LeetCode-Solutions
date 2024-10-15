# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#     def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        # Initialize the search boundaries
        left, right = 0, 1
        
        # Find the upper boundary for binary search
        while reader.get(right) < target:
            left = right
            right <<= 1  # Exponentially increase the right boundary
        
        # Perform binary search within the determined boundaries
        while left <= right:
            mid = left + (right - left) // 2
            mid_value = reader.get(mid)
            
            if mid_value == target:
                return mid
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # If the target is not found, return -1
        return -1
