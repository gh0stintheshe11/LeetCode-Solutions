class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        def gm(w):
            mk = 0
            for x in w:
                mk |= 1 << (ord(x) - ord('a'))
            return mk
        
        masks = [gm(w) for w in words]
        d = dict([(w, i) for i, w in enumerate(masks)])
        r_d = dict()
        for k, x in enumerate(masks):
            for i in range(26):
                if (x & (1 << i)) == 0: continue
                r_d[x ^ (1 << i)] = k
                
        ds = DSU(len(words))
        for u, m in enumerate(masks):
            for i in range(26):  # add remove
                if (m ^ (1 << i)) in d:
                    ds.union(u, d[(m ^ (1 << i))])
            ds.union(u, d[m])
            for i in range(26):  # replace 
                if (m & (1 << i)) == 0: continue
                nm = (m ^ (1 << i))
                if nm in r_d: ds.union(u, r_d[nm])
                
        return [ds.cnt, ds.mx]

class DSU:
    def __init__(self, N):
        self.par = list(range(N))
        self.sz = [1] * N
        self.mx = 1
        self.cnt = N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.sz[xr] < self.sz[yr]:
            xr, yr = yr, xr
        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]
        self.mx = max(self.mx, self.sz[xr])
        self.cnt -= 1
        return True