class Solution:
    def minimumLength(self, s: str) -> int:
        from collections import Counter
        
        count = Counter(s)
        for char in set(s):
            if count[char] >= 3:
                occurrences = count[char]
                count[char] = occurrences % 2 if occurrences % 2 == 1 else 2
        
        result_length = sum(count.values())
        
        return result_length