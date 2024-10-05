from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        result = []

        for i in range(len(nums)):
            # Remove indices of elements not within the window
            if deq and deq[0] == i - k:
                deq.popleft()

            # Remove from deq all elements which are smaller than the current element nums[i]
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()

            # Add the current element's index to the deq
            deq.append(i)

            # Once we have the first k elements, start adding to the result list
            if i >= k - 1:
                result.append(nums[deq[0]])  # The element at the front of the deq is the largest in the current window

        return result