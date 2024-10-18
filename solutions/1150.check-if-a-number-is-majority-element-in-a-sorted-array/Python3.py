from typing import List

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        def first_occurrence(nums, target):
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left if nums[left] == target else -1

        def last_occurrence(nums, target):
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right + 1) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid
            return left if nums[left] == target else -1

        first = first_occurrence(nums, target)
        if first == -1:
            return False
        last = last_occurrence(nums, target)

        return (last - first + 1) > len(nums) // 2