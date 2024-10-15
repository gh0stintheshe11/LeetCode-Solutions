from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Sort people by height in descending order. If heights are the same, sort by k in ascending order.
        people.sort(key=lambda x: (-x[0], x[1]))
        queue = []
        
        # Place each person in the queue at the index given by their k value.
        for p in people:
            queue.insert(p[1], p)
            
        return queue