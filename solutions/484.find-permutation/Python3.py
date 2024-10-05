class Solution:
    def findPermutation(self, s: str) -> List[int]:
        n = len(s)
        perm = list(range(1, n + 2))
        
        i = 0
        while i < len(s):
            if s[i] == 'D':
                j = i
                while j < len(s) and s[j] == 'D':
                    j += 1
                perm[i:j+1] = reversed(perm[i:j+1])
                i = j
            else:
                i += 1
        return perm