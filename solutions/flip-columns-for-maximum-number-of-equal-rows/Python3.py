from typing import List
from collections import defaultdict

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_count = defaultdict(int)
        
        for row in matrix:
            pattern = tuple(row)
            inverted_pattern = tuple(1 - x for x in row)
            pattern_count[pattern] += 1
            pattern_count[inverted_pattern] += 1
        
        return max(pattern_count.values())