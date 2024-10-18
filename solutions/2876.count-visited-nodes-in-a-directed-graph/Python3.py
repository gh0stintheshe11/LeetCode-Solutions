class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        N = len(edges)
        dp = [1]*N
        vis = [0]*N
        cycle = [0]*N 
        pathvis = [0]*N
        def dfs(i):
            vis[i] = 1
            pathvis[i] = 1
            if not vis[edges[i]]:
                dfs(edges[i])
                if not cycle[i]:
                    dp[i] = 1 + dp[edges[i]]
            elif pathvis[edges[i]] :
                d= 1
                cycle[i] = 1
                curr = edges[i]
                while curr!=i:
                    curr = edges[curr]
                    d+=1
                curr = edges[i]
                dp[i] = d
                curr = edges[i]
                while curr!=i:
                    cycle[curr] = 1
                    dp[curr] = d
                    curr = edges[curr]
            elif vis[edges[i]] and not cycle[i]:
                dp[i] = 1 + dp[edges[i]]
            pathvis[i] = 0
        for i in range(N) :
            if not vis[i] :
                dfs(i)
        return dp