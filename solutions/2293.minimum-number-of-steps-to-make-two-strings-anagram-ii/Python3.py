class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter
        
        count_s = Counter(s)
        count_t = Counter(t)
        
        steps = 0
        all_chars = set(count_s.keys()).union(set(count_t.keys()))
        
        for char in all_chars:
            steps += abs(count_s[char] - count_t[char])
        
        return steps