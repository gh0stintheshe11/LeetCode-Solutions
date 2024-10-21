class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        excess, blank = {}, []
        for i in range(3):
            for j in range(3):
                num = grid[i][j]
                if num == 1: continue
                elif num > 1: excess[(i, j)] = num
                else: blank.append((i, j))
        
        def dfs(i):
            if i == len(blank):
                return 0
            res = inf
            a, b = blank[i]
            for (x, y) in excess:
                if excess[(x, y)] == 1:
                    continue
                excess[(x, y)] -= 1
                res = min(res, dfs(i+1) + abs(x-a) + abs(y-b))
                excess[(x, y)] += 1
            return res
        return dfs(0)