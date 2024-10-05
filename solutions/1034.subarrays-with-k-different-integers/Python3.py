from typing import List
from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(k: int) -> int:
            count = defaultdict(int)
            left, result = 0, 0
            for right in range(len(nums)):
                if count[nums[right]] == 0:
                    k -= 1
                count[nums[right]] += 1
                while k < 0:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        k += 1
                    left += 1
                result += right - left + 1
            return result
        
        return atMostK(k) - atMostK(k - 1)

# Example Usage:
# sol = Solution()
# print(sol.subarraysWithKDistinct([1,2,1,2,3], 2)) # Output: 7
# print(sol.subarraysWithKDistinct([1,2,1,3,4], 3)) # Output: 3