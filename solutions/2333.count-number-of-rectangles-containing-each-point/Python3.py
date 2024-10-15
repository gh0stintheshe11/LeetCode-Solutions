from typing import List
from collections import defaultdict
import bisect

class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        # Group rectangles by height
        height_map = defaultdict(list)
        for l, h in rectangles:
            height_map[h].append(l)
        
        # Sort lengths for each height
        for h in height_map:
            height_map[h].sort()
        
        result = []
        for x, y in points:
            count = 0
            # Check all heights from y to 100
            for h in range(y, 101):
                if h in height_map:
                    # Count rectangles with length >= x using binary search
                    lengths = height_map[h]
                    pos = bisect.bisect_left(lengths, x)
                    count += len(lengths) - pos
            result.append(count)
        
        return result