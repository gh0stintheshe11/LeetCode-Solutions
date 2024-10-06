from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        max_coefficient = 0
        current_sum = 0
        total = 0

        for sat in satisfaction:
            current_sum += sat
            if current_sum + total > total:
                total += current_sum
            else:
                break
            
        return total