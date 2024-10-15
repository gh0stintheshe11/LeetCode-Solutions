from typing import List
from collections import defaultdict

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        items = sorted(zip(values, labels), key=lambda x: -x[0])
        label_count = defaultdict(int)
        max_sum = 0
        count = 0
        
        for value, label in items:
            if count == numWanted:
                break
            if label_count[label] < useLimit:
                max_sum += value
                label_count[label] += 1
                count += 1
                
        return max_sum