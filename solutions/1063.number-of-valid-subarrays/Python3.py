class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack = []
        result = 0

        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            stack.append(i)
            result += len(stack)
        
        return result