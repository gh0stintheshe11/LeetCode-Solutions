class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        visited = set()
        bfs = deque()
        dp = [[math.inf for a in range(len(grid[0]))] for y in range(len(grid))]
        dir = [(-1,0),(1,0),(0,1),(0,-1)]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]== 1:
                    visited.add((r,c))
                    dp[r][c] = 0
                    bfs.append((r,c,0))
        
        while bfs:
            r,c,h = bfs.popleft()
            for a,b in dir:
                if 0<=a+r<len(grid) and 0<=b+c<len(grid[0]) and dp[a+r][b+c] > h+1 and grid[a+r][b+c] != 2:
                    dp[a+r][b+c] = h+1
                    bfs.append((a+r,b+c,h+1))


        def pos(n):
            if n == -1:
                return True
            visited = set()
            bfs = deque()
            bfs.append((0,0,n))
            visited.add((0,0))
            dir = [(-1,0),(0,-1),(1,0),(0,1)]
            while bfs:
                r,c,h = bfs.popleft()
                if r == len(grid)-1 and c == len(grid[0])-1:
                    return True
                for a,b in dir:
                    if 0<=a+r<len(grid) and 0<=b+c<len(grid[0]) and (a+r,b+c) not in visited and grid[a+r][b+c] != 2:
                        if dp[a+r][b+c] > h+1:
                            bfs.append((a+r,b+c,h+1))
                            visited.add((a+r,b+c))
                        elif a+r==len(grid)-1 and b+c==len(grid[0])-1 and dp[a+r][b+c] == h+1:
                            return True
            return False

        l = -1
        h = int(1e9)
        while l<=h:
            mid = (l+h)//2
            if pos(mid):
                l = mid+1
            else:
                h=mid-1

        return l-1