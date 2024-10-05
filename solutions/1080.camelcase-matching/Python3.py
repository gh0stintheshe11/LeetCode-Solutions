from typing import List

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def isMatch(query: str, pattern: str) -> bool:
            i, j = 0, 0
            while i < len(query):
                if j < len(pattern) and query[i] == pattern[j]:
                    j += 1
                elif query[i].isupper():
                    return False
                i += 1
            return j == len(pattern)
        
        return [isMatch(query, pattern) for query in queries]