from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words_set = set(words)
        longest = ""
        
        for word in words:
            if all(word[:k] in words_set for k in range(1, len(word) + 1)):
                if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                    longest = word
        
        return longest