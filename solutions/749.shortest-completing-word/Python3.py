from collections import Counter
from typing import List

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        def clean_and_count(s: str) -> Counter:
            return Counter(c.lower() for c in s if c.isalpha())
        
        license_counter = clean_and_count(licensePlate)
        
        def is_completing(word: str) -> bool:
            word_counter = Counter(word)
            for letter, count in license_counter.items():
                if word_counter[letter] < count:
                    return False
            return True
        
        shortest_word = None
        
        for word in words:
            if is_completing(word):
                if shortest_word is None or len(word) < len(shortest_word):
                    shortest_word = word
        
        return shortest_word