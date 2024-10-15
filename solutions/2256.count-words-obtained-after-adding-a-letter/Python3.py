from typing import List

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        start_bitsets = set()
        
        for word in startWords:
            bitset = 0
            for ch in word:
                bitset |= 1 << (ord(ch) - ord('a'))
            start_bitsets.add(bitset)
        
        count = 0
        
        for word in targetWords:
            bitset = 0
            for ch in word:
                bitset |= 1 << (ord(ch) - ord('a'))
                
            for ch in word:
                modified_bitset = bitset ^ (1 << (ord(ch) - ord('a')))
                if modified_bitset in start_bitsets:
                    count += 1
                    break
        
        return count