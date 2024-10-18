from typing import List

class Solution:
    def findMaximums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [-1] * n
        right = [n] * n
        stack = []
        
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack.clear()
        
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        
        res = [0] * n
        for i in range(n):
            length = right[i] - left[i] - 1
            res[length - 1] = max(res[length - 1], nums[i])
        
        for i in range(n-2, -1, -1):
            res[i] = max(res[i], res[i+1])
            
        return res