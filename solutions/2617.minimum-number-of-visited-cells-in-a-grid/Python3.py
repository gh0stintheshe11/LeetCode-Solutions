class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        colheaps = [[] for j in range(n)]
        for i in range(m):
            rowheap = []
            for j in range(n):
                currmin = inf
                while rowheap and rowheap[0][1] < j:
                    heapq.heappop(rowheap)
                if rowheap:
                    currmin = min(currmin, rowheap[0][0] + 1)
                while colheaps[j] and colheaps[j][0][1] < i:
                    heapq.heappop(colheaps[j])
                if colheaps[j]:
                    currmin = min(currmin, colheaps[j][0][0] + 1)
                if i == 0 and j == 0:
                    currmin = 1
                if i == m-1 and j == n-1:
                    return currmin if currmin < inf else -1

                heapq.heappush(rowheap, (currmin, j + grid[i][j]))
                heapq.heappush(colheaps[j], (currmin, i + grid[i][j]))