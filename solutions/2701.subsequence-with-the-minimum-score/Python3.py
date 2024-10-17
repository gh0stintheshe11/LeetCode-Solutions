class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        left, right = [-1] * (n+2), [m] * (n+2)
        p = 0
        for i in range(n):
            while p < m and s[p] != t[i]: p += 1
            left[i+1] = p
            p += 1
        p = m - 1
        for i in range(n-1, -1, -1):
            while p >= 0 and s[p] != t[i]: p -= 1
            right[i+1] = p
            p -= 1

        def check(x): 
            for i in range(n + 1 - x):
                if left[i] < right[i+x+1]:
                    return True
            return False

        l, r = 0, n
        while l <= r:
            x = (l + r) // 2;
            if (check(x)): r = x - 1
            else: l = x + 1
        return l