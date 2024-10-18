from typing import List
from collections import Counter

class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums) // 2
        
        for i in range(1, len(nums)):
            k = nums[i] - nums[0]
            if k <= 0 or k % 2 != 0:
                continue
            k //= 2
            
            counts = Counter(nums)
            original = []
            for num in nums:
                if counts[num] == 0:
                    continue
                if counts[num + 2 * k] == 0:
                    break
                original.append(num + k)
                counts[num] -= 1
                counts[num + 2 * k] -= 1

            if len(original) == n:
                return original
        
        return []