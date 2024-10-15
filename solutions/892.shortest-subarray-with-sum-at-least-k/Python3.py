from collections import deque
from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]
        
        min_length = n + 1
        deque_prefix = deque()
        
        for i in range(n + 1):
            while deque_prefix and prefix_sums[i] - prefix_sums[deque_prefix[0]] >= k:
                min_length = min(min_length, i - deque_prefix.popleft())
            while deque_prefix and prefix_sums[i] <= prefix_sums[deque_prefix[-1]]:
                deque_prefix.pop()
            deque_prefix.append(i)
        
        return min_length if min_length <= n else -1