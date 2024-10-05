from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {s: i for i, s in enumerate(list1)}
        min_sum = float('inf')
        res = []
        
        for j, s in enumerate(list2):
            if s in index_map:
                i = index_map[s]
                index_sum = i + j
                if index_sum < min_sum:
                    min_sum = index_sum
                    res = [s]
                elif index_sum == min_sum:
                    res.append(s)
        
        return res