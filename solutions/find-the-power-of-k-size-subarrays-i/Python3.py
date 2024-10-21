from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        def is_consecutive_and_sorted(sub: List[int]) -> bool:
            for i in range(1, len(sub)):
                if sub[i] != sub[i-1] + 1:
                    return False
            return True
        
        n = len(nums)
        result = []
        
        for i in range(n - k + 1):
            subarray = nums[i:i+k]
            if is_consecutive_and_sorted(subarray):
                result.append(subarray[-1])
            else:
                result.append(-1)
        
        return result