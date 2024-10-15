class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        from collections import Counter
        counts = Counter(s)
        occurrences = list(counts.values())
        return all(x == occurrences[0] for x in occurrences)