from typing import List
import collections

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:

        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # depth of bob traversal path (DFS)
        self.bob_path = []
        def dfs(node, parent, path):
            if node == 0:
                self.bob_path = list(path)
                return True
            
            for nxt in graph[node]:
                if nxt == parent:
                    continue
                path.append(nxt)
                if dfs(nxt, node, path):
                    return True
                path.pop()
            
            return False
        
        dfs(bob, -1, [bob])
        step = dict()
        for index in range(len(self.bob_path)):
            step[self.bob_path[index]] = index

        # loop all possible Alice traversal path (BFS)
        ans = float('-Inf')
        profit_ini = amount[0] if bob != 0 else amount[0] // 2
        que = collections.deque([(0, -1, profit_ini)])
        depth = 0
        while que:
            for _ in range(len(que)):
                cur, parent, profit = que.popleft()
                
                if cur != 0 and len(graph[cur]) == 1:    # leaf node
                    ans = max(ans, profit)
                
                for nxt in graph[cur]:
                    if nxt == parent:
                        continue      
                    if nxt not in step or depth + 1 < step[nxt]:
                        new_profit = amount[nxt]
                    elif depth + 1 == step[nxt]:
                        new_profit = amount[nxt] // 2
                    else:
                        new_profit = 0
                    que.append((nxt, cur, profit + new_profit))

            depth += 1

        return ans