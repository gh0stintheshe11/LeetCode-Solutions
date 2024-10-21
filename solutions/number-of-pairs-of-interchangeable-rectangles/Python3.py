from typing import List
from collections import defaultdict
from fractions import Fraction

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio_count = defaultdict(int)
        pairs = 0
        
        for width, height in rectangles:
            ratio = Fraction(width, height)
            pairs += ratio_count[ratio]
            ratio_count[ratio] += 1
        
        return pairs