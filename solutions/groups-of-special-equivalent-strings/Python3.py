from typing import List

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def encode(word):
            evens = ''.join(sorted(word[::2]))
            odds = ''.join(sorted(word[1::2]))
            return (evens, odds)
        
        unique_groups = {encode(word) for word in words}
        return len(unique_groups)