from typing import List
from collections import defaultdict

class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        prefix_count = defaultdict(lambda: [0] * (n + 1))
        
        for i in range(n):
            for c in prefix_count:
                prefix_count[c][i + 1] = prefix_count[c][i]
            prefix_count[s[i]][i + 1] += 1
        
        result = []
        
        for l, r in queries:
            total_same_end = 0
            for c in prefix_count:
                count_in_range = prefix_count[c][r + 1] - prefix_count[c][l]
                total_same_end += count_in_range * (count_in_range - 1) // 2 + count_in_range
            result.append(total_same_end)
        
        return result