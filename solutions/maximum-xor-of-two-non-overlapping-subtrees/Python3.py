class Solution:
    def maxXor(self, n: int, edges: List[List[int]], values: List[int]) -> int:
        # build graph
        g = defaultdict(set)
        deg = defaultdict(int)
        
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)
            deg[a] += 1
            deg[b] += 1
        
        q = [(i, values[i]) for i in range(n) if deg[i] == 1]
        
        # compute sum for each node
        v = values[:]
        
        while q:
            node, val = q.pop()
            for nei in g[node]:
                if nei and deg[nei] == 1: continue
                v[nei] += val
                deg[nei] -= 1
                if nei and deg[nei] == 1:
                    q.append((nei, v[nei]))        
        
        # build node index at each digit
        l = v[0].bit_length()
        bits = defaultdict(lambda: defaultdict(set))
        for i, x in enumerate(v):
            x = bin(x)[2:].zfill(l)
            for j, bit in enumerate(x):
                bits[j][bit].add(i)    
        
        # check if two subtrees are overlapped
        par = [-1] * n
        def find_par(cur, p):
            for nei in g[cur]:
                if nei == p: continue
                par[nei] = cur
                find_par(nei, cur)

        find_par(0, -1)
        
        @cache
        def nonoverlap(a, b):
            x, y = a, b
            while x != -1:
                x = par[x]
                if x == b: return False
            while y != -1:
                y = par[y]
                if y == a: return False
            return True        
        
        # build from the most significant digit
        res = 0
        for k in range(l):
            if len(bits[k]) < 2: continue
            for x, y in product(bits[k]['0'], bits[k]['1']):
                if x > y: x, y = y, x
                if nonoverlap(x, y): 
                    res = max(res, v[x] ^ v[y])
            # as long as the current digit (most significant digit) could be built no need to check further
            if res: return res
        return res