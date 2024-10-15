from typing import List

class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        left = [0] * n
        right = [n] * n
        stack = []

        # Compute left limits where nums[i] is the smallest
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []

        # Compute right limits where nums[i] is the smallest
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                index = stack.pop()
                right[index] = i
            stack.append(i)

        # Find valid subarray size
        for i in range(n):
            length = right[i] - left[i] - 1
            if nums[i] > threshold / length:
                return length

        return -1