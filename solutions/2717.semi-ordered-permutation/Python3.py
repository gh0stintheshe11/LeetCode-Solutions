from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        index_1 = nums.index(1)
        index_n = nums.index(n)
        
        if index_1 < index_n:
            return index_1 + (n - index_n - 1)
        else:
            return index_1 + (n - index_n - 1) - 1