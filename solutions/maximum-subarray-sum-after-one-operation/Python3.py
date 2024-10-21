from typing import List

class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0] * nums[0]
        
        # Initialize dp arrays
        dp_no_op = [0] * n
        dp_with_op = [0] * n
        
        # Base case
        dp_no_op[0] = nums[0]
        dp_with_op[0] = nums[0] * nums[0]
        
        # Result initialized with the first element squared
        result = dp_with_op[0]
        
        for i in range(1, n):
            dp_no_op[i] = max(nums[i], dp_no_op[i - 1] + nums[i])
            dp_with_op[i] = max(nums[i] * nums[i], dp_with_op[i - 1] + nums[i], dp_no_op[i - 1] + nums[i] * nums[i])
            result = max(result, dp_with_op[i])
        
        return result