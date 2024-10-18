from typing import List, Dict
from collections import Counter

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        def word_to_bitmask(word: str) -> int:
            bitmask = 0
            for ch in word:
                bitmask |= (1 << (ord(ch) - ord('a')))
            return bitmask
        
        word_count: Dict[int, int] = Counter(word_to_bitmask(word) for word in words)
        
        result = []
        
        for puzzle in puzzles:
            first_bit = 1 << (ord(puzzle[0]) - ord('a'))
            mask = word_to_bitmask(puzzle)
            
            submask = mask
            total = 0
            while submask:
                if submask & first_bit:  # ensure first letter of puzzle is in submask
                    total += word_count.get(submask, 0)
                submask = (submask - 1) & mask
            
            result.append(total)
        
        return result