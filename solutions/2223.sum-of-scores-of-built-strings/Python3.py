class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)
        z = [0] * n
        l, r, k = 0, 0, 0
        total_score = 0
        
        for i in range(1, n):
            if i > r:
                l, r = i, i
                while r < n and s[r] == s[r - l]:
                    r += 1
                z[i] = r - l
                r -= 1
            else:
                k = i - l
                if z[k] < r - i + 1:
                    z[i] = z[k]
                else:
                    l = i
                    while r < n and s[r] == s[r - l]:
                        r += 1
                    z[i] = r - l
                    r -= 1
        
        total_score = sum(z) + n
        return total_score