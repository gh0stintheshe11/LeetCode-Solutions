from typing import List

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort()
        
        n = len(warehouse)
        left, right = 0, n - 1
        count = 0
        
        for box in reversed(boxes):
            if left <= right and box <= warehouse[right]:
                count += 1
                right -= 1
            elif left <= right and box <= warehouse[left]:
                count += 1
                left += 1
                
        return count