class Solution:
    def collectTheCoins(self, C, E):
        n = len(E) + 1
        if n == 1: return 0
        graph = [[] for _ in range(n)]
        in_degree = [0] * n
        A = deque()
        B = deque()
        vis = [False] * n
        ans = 0
        for a, b in E:
            graph[a].append(b)
            graph[b].append(a)
            in_degree[a] += 1
            in_degree[b] += 1
        for i in range(n):
            if in_degree[i] == 1:
                vis[i] = True
                if C[i] == 0:
                    A.append(i)
                else:
                    B.append(i)
        while A:
            k = A.popleft()
            for i in graph[k]:
                in_degree[i] -= 1
                if vis[i] == False and in_degree[i] == 1:
                    vis[i] = True
                    if C[i] == 0:
                        A.append(i)
                    else:
                        B.append(i)
        for _ in range(len(B)): 
            u = B.popleft()
            for i in graph[u]:
                in_degree[i] -= 1
                if vis[i] == False and in_degree[i] == 1:
                    vis[i] = True
                    B.append(i)
        for i in range(n):
            if vis[i] == False: ans += 1
        return max(0, 2 * ans - 2)