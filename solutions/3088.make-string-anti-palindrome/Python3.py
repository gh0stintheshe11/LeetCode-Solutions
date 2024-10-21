class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        n = len(s)
        from collections import Counter
        from bisect import bisect_right
        
        ct = Counter(s)
        if max(ct.values()) <= n // 2:
            s = []
            for c in sorted(ct.keys()):
                s += [c] * ct[c]
                
            c = s[0]
            start = [0]
            for i in range(1, n):
                if s[i] != c:
                    c = s[i]
                    start.append(i)
                    
            j = None
            for i in range(n // 2 - 1, -1, -1):
                if s[i] == s[n - 1 - i]:
                    if j == None:
                        j = start[bisect_right(start, i)]
                    s[n - 1 - i], s[j] = s[j], s[n - 1 - i]
                    j += 1
                else:
                    break
            return ''.join(s)
        else:
            return '-1'