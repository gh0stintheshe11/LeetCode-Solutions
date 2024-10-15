from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        num_set = set(nums)
        n = len(nums)
        duplicate = sum(nums) - sum(num_set)
        missing = sum(range(1, n+1)) - sum(num_set)
        return [duplicate, missing]