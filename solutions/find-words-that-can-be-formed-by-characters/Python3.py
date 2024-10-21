from collections import Counter
from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        total_length = 0
        
        for word in words:
            word_count = Counter(word)
            if all(chars_count[char] >= count for char, count in word_count.items()):
                total_length += len(word)
        
        return total_length