from math import ceil

class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        def computeLPSArray(pat):
            j = 0
            i = 1
            m = len(pat)
            lps = [0]*m
            while i < m:
                if pat[i] == pat[j]:
                    lps[i] = j + 1
                    i += 1
                    j += 1
                else:
                    if j != 0:
                        j = lps[j-1]
                    else:
                        i += 1 
            return lps 
        
        lps = computeLPSArray(word)
        n = len(word)
        cur = lps[-1]
        while cur and (n-cur) % k:
            cur = lps[cur-1]
        if cur:
            return (n-cur) // k
        return ceil(n / k)