
class Solution:
    def catMouseGame(self, adj: List[List[int]]) -> int:

        UNK = 0
        MOUSE_WINS = 1
        CAT_WINS = 2
        BAD = 3
        MOUSE = 0
        CAT = 1
        
        n = len(adj)
        q = deque()
        enq = set()
        W = [[[UNK]*n for _ in range(n)] for _ in range(2)]
        
        def updateNeighbors(m, c, p):
            if p == MOUSE:            
                for c2 in adj[c]:
                    if c2 == 0:
                        continue

                    if W[CAT][m][c2] == UNK:
                        state = (m, c2, CAT)
                        if state not in enq:
                            enq.add(state)
                            q.append(state)
            else:
                for m2 in adj[m]:
                    if W[MOUSE][m2][c] == UNK:
                        state = (m2, c, MOUSE)
                        if state not in enq:
                            enq.add(state)
                            q.append(state)

        for c in range(1, n):
            for p in [MOUSE, CAT]: 
                W[p][0][c] = MOUSE_WINS 
                updateNeighbors(0, c, p)

        for m in range(1, n):
            for p in [MOUSE, CAT]: 
                W[p][m][m] = CAT_WINS
                updateNeighbors(m, m, p)

        for m in range(1, n):
            for p in [MOUSE, CAT]:
                W[p][m][0] = BAD

        while q:
            state = q.popleft()
            enq.remove(state)
            m, c, p = state

            if W[p][m][c]:
                continue

            if m == c:
                raise RuntimeError("m == c: (m, c, p) =", (m, c, p))

            if p == MOUSE:
                foundUnk = False
                for m2 in adj[m]:
                    if W[CAT][m2][c] == MOUSE_WINS:
                        if m == 1 and c == 2:
                            return MOUSE_WINS
                        W[MOUSE][m][c] = MOUSE_WINS
                        updateNeighbors(m, c, MOUSE)

                        break
                    elif W[CAT][m2][c] == UNK:
                        foundUnk = True 

                if W[MOUSE][m][c] == UNK and not foundUnk:
                    if m == 1 and c == 2:
                        return CAT_WINS
                    W[MOUSE][m][c] = CAT_WINS
                    updateNeighbors(m, c, MOUSE)
                    
            else:
                foundUnk = False
                for c2 in adj[c]:
                    if c2 == 0:
                        continue
                    elif W[MOUSE][m][c2] == CAT_WINS:
                        W[CAT][m][c] = CAT_WINS 
                        updateNeighbors(m, c, CAT)
                        break
                    elif W[MOUSE][m][c2] == UNK:
                        foundUnk = True

                if W[CAT][m][c] == UNK and not foundUnk:
                    W[CAT][m][c] = MOUSE_WINS
                    updateNeighbors(m, c, CAT)

        for p in [MOUSE, CAT]:
            for m in range(n):
                for c in range(n):
                    if W[p][m][c] in [MOUSE_WINS, CAT_WINS]:
                        print(m, c, 'cat' if p else 'mouse', '->', 'MOUSE' if W[p][m][c] == MOUSE_WINS else 'CAT')

        return 0
