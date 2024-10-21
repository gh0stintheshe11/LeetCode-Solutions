class Solution:
    def countPairsOfConnectableServers(
        self, edges: List[List[int]], signalSpeed: int
    ) -> List[int]:

        def dfs(root, par, dist, graph, signalSpeed):
            count = 0
            for n, w in graph[root]:
                if n != par:
                    count += dfs(n, root, dist + w, graph, signalSpeed)
            return count + (0 if dist % signalSpeed else 1)

        graph = [[] for _ in range(len(edges) + 1)]
        for e in edges:
            graph[e[0]].append((e[1], e[2]))
            graph[e[1]].append((e[0], e[2]))
        ans = []
        for i in range(len(edges) + 1):
            nodeCount = 0
            res = 0
            nodes = []
            for n, w in graph[i]:
                t = dfs(n, i, w, graph, signalSpeed)
                nodes.append(t)
                nodeCount += t
            for count in nodes:
                res += count * (nodeCount - count)
            ans.append(res // 2)
        return ans