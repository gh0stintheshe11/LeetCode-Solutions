from collections import deque

class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        if not k:
            return sum(coins)
            
        adj = [[] for _ in range(len(coins))]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        dag = [[] for _ in range(len(coins))]
        q = deque()
        q.append(0)
        seen = set()
        seen.add(0)
        while q:
            node = q.popleft()
            for neigh in adj[node]:
                if not neigh in seen:
                    dag[node].append(neigh)
                    seen.add(neigh)
                    q.append(neigh)
        del(adj)

        memo = [[-1e10]*14 for _ in range(len(coins))]
        
        def calcMax(node, shifts):
            if shifts >= 14:
                return 0
            if memo[node][shifts] > -1e10:
                return memo[node][shifts]

            modeOne = (coins[node] >> shifts) - k
            for neigh in dag[node]:
                modeOne += calcMax(neigh, shifts)

            newShifts = shifts + 1
            modeTwo = coins[node] >> newShifts
            if shifts < 14:
                for neigh in dag[node]:
                    modeTwo += calcMax(neigh, newShifts)

            ans = max(modeOne, modeTwo)
            memo[node][shifts] = ans
            return ans

        return calcMax(0, 0)