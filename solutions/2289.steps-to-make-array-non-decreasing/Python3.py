from typing import List

class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        steps = [0] * len(nums)
        stack = []
        
        for i in reversed(range(len(nums))):
            while stack and nums[i] > nums[stack[-1]]:
                steps[i] = max(steps[i] + 1, steps[stack.pop()])
            stack.append(i)
        
        return max(steps)