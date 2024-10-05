from typing import List
from collections import defaultdict

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {x: i for i, x in enumerate(arr)}
        n = len(arr)
        longest = defaultdict(lambda: 2)
        max_len = 0
        
        for k in range(n):
            for j in range(k):
                i = index.get(arr[k] - arr[j], None)
                if i is not None and i < j:
                    longest[j, k] = longest[i, j] + 1
                    max_len = max(max_len, longest[j, k])
        
        return max_len if max_len >= 3 else 0