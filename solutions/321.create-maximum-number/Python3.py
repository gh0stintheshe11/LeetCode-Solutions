from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def merge(nums1, nums2):
            return [max(nums1, nums2).pop(0) for _ in range(len(nums1) + len(nums2))]

        def getMaxNumber(nums, k):
            drop = len(nums) - k
            stack = []
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]

        result = []
        for i in range(k + 1):
            if i <= len(nums1) and k - i <= len(nums2):
                result = max(result, merge(getMaxNumber(nums1, i), getMaxNumber(nums2, k - i)))
        return result