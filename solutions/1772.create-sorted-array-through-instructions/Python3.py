from typing import List
from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        sorted_list = SortedList()
        cost = 0
        
        for instruction in instructions:
            left = sorted_list.bisect_left(instruction)
            right = len(sorted_list) - sorted_list.bisect_right(instruction)
            cost += min(left, right)
            cost %= MOD
            sorted_list.add(instruction)
        
        return cost