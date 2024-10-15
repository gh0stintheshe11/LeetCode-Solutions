from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        if not words:
            return []

        longest_subsequence = [words[0]]

        for i in range(1, len(words)):
            if groups[i] != groups[i - 1]:
                longest_subsequence.append(words[i])
        
        return longest_subsequence