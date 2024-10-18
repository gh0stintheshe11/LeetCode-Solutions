from collections import Counter
from math import factorial

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        hn = n // 2
        if n % 2 == 0:
            hn -= 1
        res = 0
        seen = set([])
        for t in range(10**hn, 10**(hn+1)):
            st = str(t)
            if n % 2 == 1:
                st += st[:-1][::-1]
            else:
                st += st[::-1]
            it = int(st)
            ss = ''.join(sorted(st))
            if it % k != 0 or ss in seen: continue
            seen.add(ss)
            freq = Counter(st)
            curres = factorial(len(st))
            for v in freq:
                curres /= factorial(freq[v])
            if '0' in freq:
                freq['0'] -= 1
                pt = factorial(len(st)-1)
                for v in freq:
                    pt /= factorial(freq[v])
                curres -= pt
            res += curres
        return int(res)