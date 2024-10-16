
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        hand = ''.join(sorted(hand))
        
        @cache
        def fn(board, hand):
            """Return min number of balls to insert."""
            if not board: return 0
            if not hand: return inf 
            ans = inf 
            for i, ch in enumerate(hand): 
                if i == 0 or hand[i-1] != ch: 
                    hh = hand[:i] + hand[i+1:]
                    for j in range(0, len(board)): 
                        if ch == board[j] or j and board[j-1] == board[j]: 
                            bb, nn = "", board[:j] + ch + board[j:]
                            while bb != nn:
                                bb, nn = nn, ""
                                for k, grp in groupby(bb): 
                                    x = len(list(grp))
                                    if x < 3: nn += k*x
                            ans = min(ans, 1 + fn(bb, hh))
            return ans 
        
        return (lambda x: x if x < inf else -1)(fn(board, hand))
