from typing import List

class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        result = set()
        for i in range(len(phrases)):
            for j in range(len(phrases)):
                if i != j:
                    words_i = phrases[i].split()
                    words_j = phrases[j].split()
                    if words_i[-1] == words_j[0]:
                        result.add(' '.join(words_i + words_j[1:]))
        return sorted(result)