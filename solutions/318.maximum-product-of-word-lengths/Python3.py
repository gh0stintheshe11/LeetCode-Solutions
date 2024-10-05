from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        word_bits = [0] * n
        
        for i in range(n):
            for char in words[i]:
                word_bits[i] |= 1 << (ord(char) - ord('a'))
                
        max_product = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                if word_bits[i] & word_bits[j] == 0:
                    max_product = max(max_product, len(words[i]) * len(words[j]))
                    
        return max_product