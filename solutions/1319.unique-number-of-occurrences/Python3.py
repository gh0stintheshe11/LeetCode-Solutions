from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrence_count = Counter(arr)
        occurrences = list(occurrence_count.values())
        return len(occurrences) == len(set(occurrences))