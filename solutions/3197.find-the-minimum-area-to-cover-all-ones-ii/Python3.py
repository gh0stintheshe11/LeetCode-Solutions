class Solution:
    def minimumArea(self, grid: List[List[int]], x1: int, y1: int, x2: int, y2: int) -> int:
        lX = -1
        rX = -1
        uY = -1
        dY = -1
        
        for y in range(y1, y2):
            for x in range(x1, x2):
                if grid[y][x] == 1:
                    if lX == -1 or x < lX:
                        lX = x
                    
                    if rX == -1 or x > rX:
                        rX = x
                        
                    if uY == -1 or y < uY:
                        uY = y
                        
                    if dY == -1 or y > dY:
                        dY = y

        if rX == -1:
            return 0

        return (rX - lX + 1) * (dY - uY + 1)

    def minimumSum(self, grid: List[List[int]]) -> int:                
        minimum = sys.maxsize
        height = len(grid)
        width = len(grid[0])

        for y in range(1, len(grid)):
            for x in range(1, len(grid[y])):
                leftAll = self.minimumArea(grid, 0, 0, x, height)
                rightUp = self.minimumArea(grid, x, 0, width, y)
                rightDown = self.minimumArea(grid, x, y, width, height)

                a = leftAll + rightUp + rightDown

                leftUp = self.minimumArea(grid, 0, 0, x, y)
                leftDown = self.minimumArea(grid, 0, y, x, height)
                rightAll = self.minimumArea(grid, x, 0, width, height)

                b = leftUp + leftDown + rightAll

                topAll = self.minimumArea(grid, 0, 0, width, y)
                bottomAll = self.minimumArea(grid, 0, y, width, height)

                c = topAll + leftDown + rightDown
                d = bottomAll + leftUp + rightUp

                minimum = min(a, b, c, d, minimum)

        for y1 in range(height - 1):
            for y2 in range(y1 + 1, height):
                up = self.minimumArea(grid, 0, 0, width, y1)
                middle = self.minimumArea(grid, 0, y1, width, y2)
                down = self.minimumArea(grid, 0, y2, width, height)

                area = up + middle + down
                minimum = min(area, minimum)

        for x1 in range(width - 1):
            for x2 in range(x1 + 1, width):
                left = self.minimumArea(grid, 0, 0, x1, height)
                middle = self.minimumArea(grid, x1, 0, x2, height)
                right = self.minimumArea(grid, x2, 0, width, height)
            
                area = left + middle + right
                minimum = min(area, minimum)
                
        return minimum