class Solution:
    def addMinimum(self, word: str) -> int:
        ans = 0
        i = 0
        n = len(word)
        
        while i < n:
            if i < n and word[i] == 'a':
                i += 1
            else:
                ans += 1
            
            if i < n and word[i] == 'b':
                i += 1
            else:
                ans += 1

            if i < n and word[i] == 'c':
                i += 1
            else:
                ans += 1
        
        return ans