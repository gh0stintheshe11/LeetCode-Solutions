from typing import List

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Compute prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        # Calculate left and right boundaries for each index
        left = [0] * n
        right = [0] * n
        
        # Monotonic increasing stack for left boundary
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            left[i] = stack[-1] + 1 if stack else 0
            stack.append(i)
        
        # Monotonic increasing stack for right boundary
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            right[i] = stack[-1] - 1 if stack else n - 1
            stack.append(i)
        
        # Calculate the max min-product
        max_min_product = 0
        for i in range(n):
            total_sum = prefix[right[i] + 1] - prefix[left[i]]
            min_product = nums[i] * total_sum
            max_min_product = max(max_min_product, min_product)
        
        return max_min_product % MOD