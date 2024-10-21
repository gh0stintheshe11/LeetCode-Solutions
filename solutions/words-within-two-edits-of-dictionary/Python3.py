from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def within_two_edits(word1: str, word2: str) -> bool:
            diff_count = 0
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    diff_count += 1
                    if diff_count > 2:
                        return False
            return True if diff_count <= 2 else False
        
        result = []
        for query in queries:
            for word in dictionary:
                if within_two_edits(query, word):
                    result.append(query)
                    break
        return result