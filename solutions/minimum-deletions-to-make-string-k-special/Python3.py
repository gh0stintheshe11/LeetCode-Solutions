class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        from collections import Counter

        freq = Counter(word)
        freq_values = list(freq.values())
        freq_values.sort()
        
        min_deletions = float('inf')
        n = len(freq_values)
        
        for i in range(n):
            x = freq_values[i]
            deletions = 0
            
            for j in range(n):
                y = freq_values[j]
                if y < x:
                    deletions += y
                elif y > x + k:
                    deletions += y - (x + k)
            
            min_deletions = min(min_deletions, deletions)
        
        return min_deletions