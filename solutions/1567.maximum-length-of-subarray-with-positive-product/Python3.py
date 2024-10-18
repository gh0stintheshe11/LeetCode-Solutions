from typing import List

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        max_length = 0
        current_positive = 0
        current_negative = 0
        
        for num in nums:
            if num == 0:
                current_positive, current_negative = 0, 0
            elif num > 0:
                current_positive += 1
                current_negative = current_negative + 1 if current_negative > 0 else 0
            else:
                new_positive = current_negative + 1 if current_negative > 0 else 0
                current_negative = current_positive + 1
                current_positive = new_positive
            
            max_length = max(max_length, current_positive)
        
        return max_length