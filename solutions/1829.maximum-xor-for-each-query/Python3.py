from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_xor = (1 << maximumBit) - 1
        prefix_xor = 0
        result = []
        
        for num in nums:
            prefix_xor ^= num
        
        for num in reversed(nums):
            result.append(prefix_xor ^ max_xor)
            prefix_xor ^= num
            
        return result