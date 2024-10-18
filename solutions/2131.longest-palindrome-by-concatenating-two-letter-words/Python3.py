from collections import Counter
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        length = 0
        center_added = False
        
        for word, freq in count.items():
            if word[0] == word[1]:
                pairs = freq // 2
                length += pairs * 4
                if freq % 2 == 1 and not center_added:
                    length += 2
                    center_added = True
            else:
                rev_word = word[::-1]
                if rev_word in count:
                    pairs = min(freq, count[rev_word])
                    length += pairs * 4
                    count[rev_word] = 0  # To avoid double counting
        
        return length