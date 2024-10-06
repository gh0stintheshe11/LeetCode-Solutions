from collections import deque
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()
        min_deque = deque()
        left = 0
        result = 0
        
        for right in range(len(nums)):
            while max_deque and nums[max_deque[-1]] < nums[right]:
                max_deque.pop()
            while min_deque and nums[min_deque[-1]] > nums[right]:
                min_deque.pop()
                
            max_deque.append(right)
            min_deque.append(right)
            
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                if max_deque[0] == left:
                    max_deque.popleft()
                if min_deque[0] == left:
                    min_deque.popleft()
                left += 1

            result = max(result, right - left + 1)
        
        return result