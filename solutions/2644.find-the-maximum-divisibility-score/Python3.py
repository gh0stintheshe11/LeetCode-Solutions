from typing import List

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        max_score = -1
        best_divisor = None
        
        for divisor in divisors:
            score = sum(num % divisor == 0 for num in nums)
            if score > max_score or (score == max_score and (best_divisor is None or divisor < best_divisor)):
                max_score = score
                best_divisor = divisor
                
        return best_divisor