import random
from typing import List

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.areas = []
        self.total_area = 0
        
        for rect in rects:
            area = (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1)
            self.total_area += area
            self.areas.append(self.total_area)

    def pick(self) -> List[int]:
        rand_area = random.randint(1, self.total_area)
        left, right = 0, len(self.areas) - 1
        
        while left < right:
            mid = (left + right) // 2
            if self.areas[mid] < rand_area:
                left = mid + 1
            else:
                right = mid
        
        rect = self.rects[left]
        x = random.randint(rect[0], rect[2])
        y = random.randint(rect[1], rect[3])
        
        return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()