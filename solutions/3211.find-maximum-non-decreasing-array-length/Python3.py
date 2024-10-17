from itertools import accumulate
from collections import deque

class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        prefix_sums = list(accumulate(nums, initial=0))
        queue = deque()
        prev = 0
        for i, val in enumerate(nums, 1):
            while queue and queue[0][0] >= -prefix_sums[i]:
                _, prev = queue.popleft()
            dp[i] = dp[prev] + 1
            cost = -prefix_sums[i] - (prefix_sums[i] - prefix_sums[prev])
            while queue and queue[-1][0] <= cost:
                queue.pop()                      
            queue.append([cost, i])
        return dp[-1]