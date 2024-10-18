class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        n = len(s)
        
        for i in range(n):
            if s[i] == '?':
                for c in 'abc':
                    if (i > 0 and s[i - 1] == c) or (i < n - 1 and s[i + 1] == c):
                        continue
                    s[i] = c
                    break
        
        return ''.join(s)