from typing import List

class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        n = len(nums)
        count = 0
        
        for i in range(n):
            remainder_count = [0] * d
            
            for j in range(i + 1, n):
                target_rem = (-nums[i] - nums[j]) % d
                count += remainder_count[target_rem]
                
                remainder_count[nums[j] % d] += 1
                
        return count