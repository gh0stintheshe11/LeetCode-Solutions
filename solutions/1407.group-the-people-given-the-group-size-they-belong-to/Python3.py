from typing import List
from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_map = defaultdict(list)
        result = []
        
        for person, size in enumerate(groupSizes):
            group_map[size].append(person)
            if len(group_map[size]) == size:
                result.append(group_map[size])
                group_map[size] = []
        
        return result