MX = 100001
lpf = [0] * MX
for i in range(2, MX):
    if lpf[i] == 0:
        for j in range(i, MX, i):
            lpf[j] = i

class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:set([]) for i in range(1,n+1)}
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        isprimes = [lpf[i] == i for i in range(1,n+1)]
        p = {i:-1 for i in range(1,n+1)}
        def reroot(node,pnode):
            p[node] = pnode
            for child in graph[node]:
                if child!=pnode:
                    reroot(child,node)
        
        reroot(1,None)
        self.res = 0
        
        @cache 
        def dp(node):
            with_p,without_p = 0,0
            if isprimes[node-1]:
                with_p = 1
            else:
                without_p = 1
            for child in graph[node]:
                if child!=p[node]:
                    a,b = dp(child)
                    if isprimes[node-1]:
                        self.res += with_p*b
                        with_p += b
                    else:
                        with_p += a
                        without_p += b
            if not isprimes[node-1]:
                for child in graph[node]:
                    if child!=p[node]:
                        a,b = dp(child)
                        self.res += a*(without_p - b)
            return with_p,without_p
                    
        dp(1)
        return self.res