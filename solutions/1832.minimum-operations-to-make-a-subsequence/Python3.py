from typing import List
import bisect

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        # Map the target values to their indices
        target_index_map = {value: idx for idx, value in enumerate(target)}
        
        # Translate arr into indices from target's perspective
        index_list = [target_index_map[val] for val in arr if val in target_index_map]
        
        # Find the length of the Longest Increasing Subsequence in index_list
        lis = []
        for index in index_list:
            pos = bisect.bisect_left(lis, index)
            if pos < len(lis):
                lis[pos] = index
            else:
                lis.append(index)

        # The minimum operations needed is the difference
        return len(target) - len(lis)