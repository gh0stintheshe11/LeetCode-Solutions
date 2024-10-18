from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor_sum = 0
        for num in nums:
            xor_sum ^= num

        diff = xor_sum ^ k
        operations = 0
        
        while diff > 0:
            operations += diff & 1
            diff >>= 1
            
        return operations