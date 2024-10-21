from typing import List

class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = sorted(set(nums))
        sum_k = k * (k + 1) // 2
        
        for num in nums:
            if num <= k:
                sum_k += k + 1 - num
                k += 1
            else:
                break
        
        return sum_k