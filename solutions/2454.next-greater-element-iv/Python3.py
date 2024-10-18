from typing import List
from collections import deque

class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack1 = []
        stack2 = []

        for i in range(n):
            while stack2 and nums[stack2[-1]] < nums[i]:
                result[stack2.pop()] = nums[i]

            temp = deque()
            while stack1 and nums[stack1[-1]] < nums[i]:
                temp.append(stack1.pop())

            while temp:
                stack2.append(temp.pop())

            stack1.append(i)

        return result