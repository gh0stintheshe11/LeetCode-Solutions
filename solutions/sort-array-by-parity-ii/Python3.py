from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        even_idx, odd_idx = 0, 1
        
        for num in nums:
            if num % 2 == 0:
                result[even_idx] = num
                even_idx += 2
            else:
                result[odd_idx] = num
                odd_idx += 2
                
        return result