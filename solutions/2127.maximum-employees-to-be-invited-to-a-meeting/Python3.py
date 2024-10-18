class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        graph = [[] for _ in range(n)]
        for i in range(n):
            graph[favorite[i]].append(i)
        visited = [0] * n
        level = [0] * n

        def dfs(node: int, l: int) -> int:
            if visited[node] == 2:
                return 0
            if visited[node] == 1:
                return l - level[node]
            level[node] = l
            visited[node] = 1
            ans = 0
            for child in graph[node]:
                ans = max(ans, dfs(child, l + 1))
            visited[node] = 2
            return ans
        
        maxCycle = 0
        for i in range(n):
            maxCycle = max(maxCycle, dfs(i, 0))

        def dfs2(node: int, parent: int) -> int:
            ans = 1
            for child in graph[node]:
                if child != parent:
                    ans = max(ans, 1 + dfs2(child, node))
            return ans 
    
        twoNodeAns = 0 
        for u in range(n):
            for v in graph[u]:
                if u in graph[v]:
                    twoNodeAns += dfs2(u, v) + dfs2(v, u)
        
        return max(twoNodeAns // 2, maxCycle)