class UF:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
        self.dis = dict()

    def find(self,n):
        n = self.par[n]
        while n != self.par[n]:
            self.par[n] = self.par[self.par[n]]
            n = self.par[n]
        return n
    
    def short(self,n1,n2):
        p1, p2 = self.find(n1), self.find(n2)
        return -1 if p1 != p2 else self.dis[p1]

    def union(self,n1,n2,weight):
        p1, p2 = self.find(n1), self.find(n2)
        small, big = sorted([p1,p2], key = lambda x: self.rank[x])
        if big not in self.dis:
            self.dis[big] = weight
        if small not in self.dis:
            self.dis[small] = weight
        self.dis[big] = self.dis[big] & weight & self.dis[small]
        if p1 == p2:
            return True
        self.par[small] = big
        self.rank[big] += self.rank[small]

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        uf = UF(n)
        res = []
        for n1,n2,w in edges:
            uf.union(n1,n2,w)
        for q1, q2 in query:
            res.append(uf.short(q1,q2))
        return res