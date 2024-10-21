from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_map = {0: -1}
        total_sum = 0
        
        for i, num in enumerate(nums):
            total_sum += num
            mod_value = total_sum % k
            
            if mod_value in mod_map:
                if i - mod_map[mod_value] > 1:
                    return True
            else:
                mod_map[mod_value] = i
                
        return False