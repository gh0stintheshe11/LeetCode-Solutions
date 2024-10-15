from typing import List
import collections

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        deq = collections.deque([0])
        for i in range(1, n):
            nums[i] += nums[deq[0]]
            while deq and nums[deq[-1]] <= nums[i]:
                deq.pop()
            deq.append(i)
            if deq[0] == i - k:
                deq.popleft()
        return nums[-1]