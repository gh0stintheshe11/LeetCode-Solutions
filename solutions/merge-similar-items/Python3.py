from typing import List

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        weight_map = {}
        
        for value, weight in items1:
            weight_map[value] = weight_map.get(value, 0) + weight
            
        for value, weight in items2:
            weight_map[value] = weight_map.get(value, 0) + weight
            
        result = [[value, weight] for value, weight in sorted(weight_map.items())]
        
        return result