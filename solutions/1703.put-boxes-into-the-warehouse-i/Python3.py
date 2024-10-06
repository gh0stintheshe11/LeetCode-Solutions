from typing import List

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        # Sort the boxes in descending order for optimal arrangement
        boxes.sort(reverse=True)
        
        # Calculate the effective height restrictions from leftmost to rightmost rooms
        effective_heights = [warehouse[0]]
        for i in range(1, len(warehouse)):
            effective_heights.append(min(effective_heights[-1], warehouse[i]))

        # Attempt to fit each box into the warehouse from the rightmost to leftmost
        box_index = len(boxes) - 1
        count = 0

        for i in range(len(warehouse) - 1, -1, -1):
            if box_index >= 0 and boxes[box_index] <= effective_heights[i]:
                count += 1
                box_index -= 1

        return count