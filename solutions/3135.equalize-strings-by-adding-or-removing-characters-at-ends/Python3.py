class Solution:
    def minOperations(self, s: str, t: str) -> int:

        m, n = len(s), len(t)
        if m < n:   return self.minOperations(t, s)

        def check(l: int) -> bool:
            hSet, hVal, power = set(), 0, pow(p,l,mod)

            for i in range(l):
                hVal = (hVal*p+t[i]) % mod
            hSet.add(hVal)
            for i, c in enumerate(t[l:]):
                hVal = (hVal*p+c-t[i]*power) % mod
                hSet.add(hVal)

            hVal = 0
            for i in range(l):
                hVal = (hVal*p+s[i]) % mod
            for i,c in enumerate(s[l:]):
                if hVal in hSet:    return False
                hVal = (hVal*p+c-s[i]*power) % mod
            return hVal not in hSet

        s, t = [ord(c)-97 for c in s], [ord(c)-97 for c in t]
        p, mod = 26, (1<<31)-1
        return m + n - 2 * bisect_left(range(1,n+1), 1, key=check)