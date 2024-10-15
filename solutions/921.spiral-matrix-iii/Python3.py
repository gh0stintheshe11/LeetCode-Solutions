class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        step_size = 1
        x, y = rStart, cStart
        result = [[x, y]]
        
        while len(result) < rows * cols:
            for idx in range(4):
                dx, dy = directions[idx]
                step_size_increase = idx % 2
                
                for _ in range(step_size):
                    x += dx
                    y += dy
                    if 0 <= x < rows and 0 <= y < cols:
                        result.append([x, y])
                
                if step_size_increase == 1:
                    step_size += 1
        
        return result