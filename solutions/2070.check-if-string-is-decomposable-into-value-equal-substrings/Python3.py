class Solution:
    def isDecomposable(self, s: str) -> bool:
        n = len(s)
        count2 = 0
        i = 0
        
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            length = j - i
            
            if length % 3 == 1:
                return False
            elif length % 3 == 2:
                count2 += 1
                if count2 > 1:
                    return False
            
            i = j
        
        return count2 == 1