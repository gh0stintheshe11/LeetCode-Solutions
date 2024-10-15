from typing import List

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        current_sum = 0
        count = 0
        
        for number in range(1, n + 1):
            if number not in banned_set:
                if current_sum + number > maxSum:
                    break
                current_sum += number
                count += 1
        
        return count