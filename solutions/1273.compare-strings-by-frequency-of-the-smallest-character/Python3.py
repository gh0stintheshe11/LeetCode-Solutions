from typing import List
from bisect import bisect_right

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s: str) -> int:
            return s.count(min(s))

        word_frequencies = sorted(f(word) for word in words)

        result = []
        for query in queries:
            query_frequency = f(query)
            # Count the number of word frequencies greater than query frequency
            count = len(word_frequencies) - bisect_right(word_frequencies, query_frequency)
            result.append(count)
        
        return result