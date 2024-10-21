class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        firstPlayer, secondPlayer = firstPlayer-1, secondPlayer-1 # 0-indexed
        
        @cache
        def fn(k, mask): 
            """Return earliest and latest rounds."""
            can = deque()
            for i in range(n): 
                if mask & (1 << i): can.append(i)
                    
            cand = [] # eliminated player
            while len(can) > 1: 
                p1, p2 = can.popleft(), can.pop()
                if p1 == firstPlayer and p2 == secondPlayer or p1 == secondPlayer and p2 == firstPlayer: return [k, k] # game of interest 
                if p1 in (firstPlayer, secondPlayer): cand.append([p2]) # p2 eliminated 
                elif p2 in (firstPlayer, secondPlayer): cand.append([p1]) # p1 eliminated 
                else: cand.append([p1, p2]) # both could be elimited 
            
            minn, maxx = inf, -inf
            for x in product(*cand): 
                mask0 = mask
                for i in x: mask0 ^= 1 << i
                mn, mx = fn(k+1, mask0)
                minn = min(minn, mn)
                maxx = max(maxx, mx)
            return minn, maxx
        
        return fn(1, (1<<n)-1)