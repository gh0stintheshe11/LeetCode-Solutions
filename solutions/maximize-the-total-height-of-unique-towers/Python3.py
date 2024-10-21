from typing import List

class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        n = len(maximumHeight)
        max_possible_height = float('inf')
        total_sum = 0
        
        for height in maximumHeight:
            # The current height can only be as much as one smaller than the previous, but not more than the maximum that tower can be
            if max_possible_height > height:
                max_possible_height = height
            total_sum += max_possible_height
            max_possible_height -= 1

            if max_possible_height < 0:
                return -1

        return total_sum