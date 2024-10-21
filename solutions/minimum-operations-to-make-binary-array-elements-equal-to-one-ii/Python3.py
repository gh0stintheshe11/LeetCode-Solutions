from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        flip_state = 0

        for num in nums:
            if num == flip_state:
                operations += 1
                flip_state = 1 - flip_state
        
        return operations