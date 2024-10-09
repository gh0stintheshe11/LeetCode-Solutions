from typing import List

class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        common_set = set(arrays[0])
        
        for array in arrays[1:]:
            common_set.intersection_update(array)
        
        return sorted(common_set)