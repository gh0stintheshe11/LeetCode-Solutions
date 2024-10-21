from typing import List
from collections import defaultdict

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        def build_prefix_table(words):
            prefix_table = defaultdict(list)
            for word in words:
                for i in range(len(word) + 1):
                    prefix_table[word[:i]].append(word)
            return prefix_table

        def backtrack(step):
            if step == n:
                results.append(square[:])
                return
            prefix = ''.join(square[i][step] for i in range(step))
            for candidate in prefix_table[prefix]:
                square.append(candidate)
                backtrack(step + 1)
                square.pop()

        n = len(words[0])
        prefix_table = build_prefix_table(words)
        results = []
        square = []

        for word in words:
            square.append(word)
            backtrack(1)
            square.pop()

        return results