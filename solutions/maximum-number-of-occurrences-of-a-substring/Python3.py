class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        from collections import defaultdict
        
        freq_map = defaultdict(int)
        max_occurrences = 0
        
        for i in range(len(s) - minSize + 1):
            substring = s[i:i + minSize]
            if len(set(substring)) <= maxLetters:
                freq_map[substring] += 1
                max_occurrences = max(max_occurrences, freq_map[substring])
        
        return max_occurrences