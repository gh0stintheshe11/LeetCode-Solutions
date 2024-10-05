from typing import List

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(bound: int) -> int:
            ans = curr = 0
            for num in nums:
                if num <= bound:
                    curr += 1
                else:
                    curr = 0
                ans += curr
            return ans
        
        return count(right) - count(left - 1)