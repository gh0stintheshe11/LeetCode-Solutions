from typing import List

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_subsequence(x):
            it = iter(s)
            return all(c in it for c in x)

        dictionary.sort(key=lambda x: (-len(x), x))
        for word in dictionary:
            if is_subsequence(word):
                return word
        return ""