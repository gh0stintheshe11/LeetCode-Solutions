from typing import List

class DistanceLimitedPathsExist:

    def __init__(self, n: int, edgeList: List[List[int]]):
        edgeList.sort(key=lambda x: x[2])
        self.parent = list(range(n))
        self.rank = [0] * n
        self.max_edge = [{} for _ in range(n)]

        def find(u):
            if u != self.parent[u]:
                self.parent[u] = find(self.parent[u])
            return self.parent[u]

        def union(u, v, weight):
            rootU = find(u)
            rootV = find(v)
            if rootU != rootV:
                if self.rank[rootU] > self.rank[rootV]:
                    self.parent[rootV] = rootU
                elif self.rank[rootU] < self.rank[rootV]:
                    self.parent[rootU] = rootV
                else:
                    self.parent[rootV] = rootU
                    self.rank[rootU] += 1
                self.max_edge[rootU][rootV] = weight
                self.max_edge[rootV][rootU] = weight

        for u, v, dis in edgeList:
            union(u, v, dis)

    def query(self, p: int, q: int, limit: int) -> bool:
        def dfs(node, target, max_dis, visited):
            if node == target:
                return True
            visited.add(node)
            for nei, weight in self.max_edge[node].items():
                if nei not in visited and weight < limit:
                    if dfs(nei, target, max(weight, max_dis), visited):
                        return True
            return False
        
        return dfs(p, q, 0, set())