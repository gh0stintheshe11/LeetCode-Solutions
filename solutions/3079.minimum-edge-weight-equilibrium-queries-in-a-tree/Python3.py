class BinaryLifting:
    def __init__(self, n, edges):
        self.n = n
        self.LOG = n.bit_length()
        self.C = 27
        self.graph = defaultdict(list)
        self.parent = [[-1] * n for _ in range(self.LOG)]
        self.depth = [0] * n
        self.weight_count = [[0] * self.C for _ in range(n)]
        self._build_graph(edges)
        self._preprocess()

    def _build_graph(self, edges):
        for u, v, w in edges:
            self.graph[u].append((v, w))
            self.graph[v].append((u, w))

    def _dfs(self, node, par):
        self.parent[0][node] = par
        for neighbor, weight in self.graph[node]:
            if neighbor == par:
                continue
            self.depth[neighbor] = self.depth[node] + 1
            self.weight_count[neighbor] = self.weight_count[node].copy()
            self.weight_count[neighbor][weight] += 1
            self._dfs(neighbor, node)

    def _preprocess(self):
        self._dfs(0, -1)
        for i in range(1, self.LOG):
            for j in range(self.n):
                if self.parent[i - 1][j] != -1:
                    self.parent[i][j] = self.parent[i - 1][self.parent[i - 1][j]]

    def get_kth_ancestor(self, node, k):
        for i in range(self.LOG):
            if k & (1 << i):
                node = self.parent[i][node]
                if node == -1:
                    break
        return node

    def lca(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        diff = self.depth[u] - self.depth[v]
        u = self.get_kth_ancestor(u, diff)
        if u == v:
            return u
        for i in range(self.LOG - 1, -1, -1):
            if self.parent[i][u] != self.parent[i][v]:
                u = self.parent[i][u]
                v = self.parent[i][v]
        return self.parent[0][u]

    def min_operations_queries(self, queries: List[List[int]]) -> List[int]:
        res = []
        for x, y in queries:
            l = self.lca(x, y)
            length = self.depth[x] + self.depth[y] - 2 * self.depth[l]
            max_z = max(self.weight_count[x][z] + self.weight_count[y][z] - 2 * self.weight_count[l][z] for z in range(self.C))
            res.append(length - max_z)
        return res

class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        bl = BinaryLifting(n, edges)
        return bl.min_operations_queries(queries)