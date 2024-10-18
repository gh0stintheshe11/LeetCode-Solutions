from typing import List
from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        
        for r in range(len(nums)):
            for c in range(len(nums[r])):
                diagonals[r + c].append(nums[r][c])
        
        result = []
        for k in sorted(diagonals.keys()):
            result.extend(reversed(diagonals[k]))
        
        return result