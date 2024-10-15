from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        special = [0] * n
        
        # Initialize first partition
        special[0] = 1
        
        # Construct the special partitions
        for i in range(1, n):
            if (nums[i] % 2) != (nums[i - 1] % 2):
                special[i] = special[i - 1]
            else:
                special[i] = special[i - 1] + 1
        
        result = []
        for fromi, toi in queries:
            result.append(special[fromi] == special[toi])
        
        return result