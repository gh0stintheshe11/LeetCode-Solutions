class Solution:
    def countWinningSequences(self, s: str) -> int:
    
        MOD = 10**9 + 7

        wins = {'W': 'F', 'E':'W', 'F':'E'}
        loss = {'F': 'W', 'W':'E', 'E':'F'}

        @cache
        def solve(idx, prev_val, bob):
            if idx == len(s):
                return 1 if bob > 0 else 0

            res = 0
            for move in {'F', 'E', 'W'}:
                if move != prev_val and wins[move] == s[idx]:
                    res += solve(idx + 1, move, bob + 1)
                elif move != prev_val and loss[move] == s[idx]:
                    res += solve(idx + 1, move, bob - 1)
                elif move != prev_val and move == s[idx]:
                    res += solve(idx + 1, move, bob)

            return res % MOD

        return solve(0, "None", 0) % MOD