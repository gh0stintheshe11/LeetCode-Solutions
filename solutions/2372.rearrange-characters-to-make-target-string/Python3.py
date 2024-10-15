from collections import Counter

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        count_s = Counter(s)
        count_target = Counter(target)
        
        max_copies = float('inf')
        
        for char in count_target:
            max_copies = min(max_copies, count_s.get(char, 0) // count_target[char])
        
        return max_copies