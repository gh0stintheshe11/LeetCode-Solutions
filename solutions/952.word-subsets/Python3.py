from typing import List
from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count_max_freq(words: List[str]) -> Counter:
            max_freq = Counter()
            for word in words:
                freq = Counter(word)
                for letter, count in freq.items():
                    max_freq[letter] = max(max_freq[letter], count)
            return max_freq
        
        b_max_freq = count_max_freq(words2)
        
        def is_universal(word: str) -> bool:
            word_freq = Counter(word)
            for letter, count in b_max_freq.items():
                if word_freq[letter] < count:
                    return False
            return True
        
        return [word for word in words1 if is_universal(word)]