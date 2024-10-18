from itertools import combinations
from collections import Counter
from typing import List

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        max_score = 0
        letter_count = Counter(letters)
        
        def word_score(word):
            return sum(score[ord(c) - ord('a')] for c in word)

        def can_form(word, available):
            word_count = Counter(word)
            return all(word_count[c] <= available[c] for c in word_count)
        
        def backtrack(index, available, current_score):
            nonlocal max_score
            if index == len(words):
                max_score = max(max_score, current_score)
                return
            # skip the current word
            backtrack(index + 1, available, current_score)
            # take the current word if possible
            word = words[index]
            if can_form(word, available):
                new_available = available - Counter(word)
                backtrack(index + 1, new_available, current_score + word_score(word))
        
        backtrack(0, letter_count, 0)
        
        return max_score