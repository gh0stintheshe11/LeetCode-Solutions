class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_bound = [-1] * n
        right_bound = [n] * n
        stack = []

        # Find left bounds
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            if stack:
                left_bound[i] = stack[-1]
            stack.append(i)

        stack = []

        # Find right bounds
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            if stack:
                right_bound[i] = stack[-1]
            stack.append(i)

        ans = [0] * n
        for i in range(n):
            ans[i] = right_bound[i] - left_bound[i] - 1

        return ans