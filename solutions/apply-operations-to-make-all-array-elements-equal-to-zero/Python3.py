from typing import List

class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        operations = [0] * (n + 1)
        current_subtract = 0
        
        for i in range(n):
            current_subtract += operations[i]
            nums[i] -= current_subtract
            
            if nums[i] < 0:
                return False
            
            if nums[i] > 0:
                if i + k > n:
                    return False
                operations[i] += nums[i]
                operations[i + k] -= nums[i]
                current_subtract += nums[i]
        
        return True