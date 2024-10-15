from typing import List

class Solution:
    def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        length = len(nums)
        result = []

        for time, index in queries:
            cycle_length = 2 * length
            
            if time % cycle_length < length:
                # In the shrinking phase
                remaining_length = length - (time % cycle_length)
                if index < remaining_length:
                    result.append(nums[index + (time % cycle_length)])
                else:
                    result.append(-1)
            else:
                # In the growing phase
                growing_index = time % length
                if index < growing_index:
                    result.append(nums[index])
                else:
                    result.append(-1)

        return result