class Solution:
    def minimumDistance(self, word: str) -> int:
        def get_pos(c):
            return divmod(ord(c) - ord('A'), 6)
        
        def dist(c1, c2):
            x1, y1 = get_pos(c1)
            x2, y2 = get_pos(c2)
            return abs(x1 - x2) + abs(y1 - y2)
        
        n = len(word)
        dp = {}
        
        def dfs(i, f1, f2):
            if i == n:
                return 0
            if (i, f1, f2) in dp:
                return dp[(i, f1, f2)]
            
            f1_pos = word[f1] if f1 is not None else None
            f2_pos = word[f2] if f2 is not None else None
            
            move_f1 = dist(f1_pos, word[i]) if f1_pos is not None else 0
            move_f2 = dist(f2_pos, word[i]) if f2_pos is not None else 0
            
            cost_f1 = (move_f1 + dfs(i + 1, i, f2))
            cost_f2 = (move_f2 + dfs(i + 1, f1, i))
            
            ans = min(cost_f1, cost_f2)
            dp[(i, f1, f2)] = ans
            return ans
        
        return dfs(0, None, None)