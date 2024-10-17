from typing import List
import heapq

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        sum_val = sum(nums)
        nums = [-x for x in nums]  # convert to min-heap
        heapq.heapify(nums)
        
        while len(nums) > 2:
            num = heapq.heappop(nums)
            if sum_val > 2 * (-num):
                return sum_val
            sum_val -= (-num)
        
        return -1