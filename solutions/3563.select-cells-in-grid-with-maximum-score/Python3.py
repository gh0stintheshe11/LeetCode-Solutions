class Solution:
    def maxScore(self, grid: List[List[int]]) -> int: 
        H = [set([]) for i in range(101)]
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                H[grid[i][j]].add(2**i)
        d = [0 for i in range(2**10)]
        for i in range(101):
            new_d = [x for x in d]
            for x in range(2**10):
                for y in H[i]:
                    if y|x != x:
                        x2 = y|x
                        new_d[x2] = max(new_d[x2], i+d[x])
            d = new_d
        return max(d)