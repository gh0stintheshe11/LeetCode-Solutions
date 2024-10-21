class Solution:
    def minEdgeReversals(self, N: int, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append((v, 0))
            graph[v].append((u, 1))
        
        ans = [0] * N

        def subtree_counts(root, prev):
            for v, w in graph[root]:
                if v != prev:
                    subtree_counts(v, root)
                    ans[0] += w
        
        def get_dist(u, prev):
            for v, w in graph[u]:
                if v != prev:
                    ans[v] = ans[u]
                    if w == 0:
                        ans[v] += 1
                    else:
                        ans[v] -= 1
                    get_dist(v, u)

        subtree_counts(0, -1)
        get_dist(0, -1)
        
        return ans