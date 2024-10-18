from typing import List
from collections import deque

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        queue = deque()
        opened = set()
        availableKeys = set()
        availableBoxes = set(initialBoxes)
        totalCandies = 0

        for box in initialBoxes:
            if status[box] == 1:
                queue.append(box)

        while queue:
            current_box = queue.popleft()
            if current_box in opened:
                continue
            totalCandies += candies[current_box]
            opened.add(current_box)
            for key in keys[current_box]:
                availableKeys.add(key)
            for inner_box in containedBoxes[current_box]:
                availableBoxes.add(inner_box)
                if inner_box in availableKeys or status[inner_box] == 1:
                    queue.append(inner_box)
            for new_key in availableKeys:
                if new_key in availableBoxes and new_key not in opened:
                    queue.append(new_key)

        return totalCandies