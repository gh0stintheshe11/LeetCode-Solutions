from typing import List

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def compute_sum(divisor: int) -> int:
            return sum((num + divisor - 1) // divisor for num in nums)
        
        left, right = 1, max(nums)
        
        while left < right:
            mid = (left + right) // 2
            if compute_sum(mid) <= threshold:
                right = mid
            else:
                left = mid + 1
        
        return left
