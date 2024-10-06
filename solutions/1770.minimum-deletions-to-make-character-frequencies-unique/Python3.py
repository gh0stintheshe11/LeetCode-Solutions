class Solution:
    def minDeletions(self, s: str) -> int:
        from collections import Counter
        
        freq = Counter(s)
        frequencies = list(freq.values())
        used_frequencies = set()
        deletions = 0
        
        for f in frequencies:
            while f > 0 and f in used_frequencies:
                f -= 1
                deletions += 1
            used_frequencies.add(f)
        
        return deletions