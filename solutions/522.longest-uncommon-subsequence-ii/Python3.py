from typing import List

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subsequence(s, t):
            t = iter(t)
            return all(c in t for c in s)

        strs.sort(key=len, reverse=True)
        
        for i, s in enumerate(strs):
            if all(not is_subsequence(s, strs[j]) for j in range(len(strs)) if i != j):
                return len(s)
        
        return -1