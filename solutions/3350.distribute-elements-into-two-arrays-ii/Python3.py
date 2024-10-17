from sortedcontainers import SortedList
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        def gc(n):
            if len(sl1) - sl1.bisect_right(n) == len(sl2) - sl2.bisect_right(n):
                return len(sl1) <= len(sl2)
            return len(sl1) - sl1.bisect_right(n) > len(sl2) - sl2.bisect_right(n)
        
        sl1 = SortedList([nums[0]])
        sl2 = SortedList([nums[1]])
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        
        for i in range(2, len(nums)):
            if gc(nums[i]):
                sl1.add(nums[i])
                arr1.append(nums[i])
            else:
                sl2.add(nums[i])
                arr2.append(nums[i])
        
        return arr1 + arr2