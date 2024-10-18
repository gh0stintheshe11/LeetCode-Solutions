from typing import List

class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        
        left_max = [None] * n
        right_min = [None] * n
        
        left_max[0] = nums[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], nums[i-1])
        
        right_min[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            right_min[i] = min(right_min[i+1], nums[i+1])
        
        count = 0
        for i in range(n):
            if (i == 0 or nums[i] > left_max[i]) and (i == n-1 or nums[i] < right_min[i]):
                count += 1

        return count