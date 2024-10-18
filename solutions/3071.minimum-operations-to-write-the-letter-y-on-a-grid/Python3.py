class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        center = n // 2
        
        y_cells = set()
        
        for i in range(center):
            y_cells.add((i, i))
            y_cells.add((i, n - 1 - i))
        
        for i in range(center, n):
            y_cells.add((i, center))
        
        def calculate_operations(value_at_Y, value_at_non_Y):
            operations = 0
            for i in range(n):
                for j in range(n):
                    if (i, j) in y_cells:
                        if grid[i][j] != value_at_Y:
                            operations += 1
                    else:
                        if grid[i][j] != value_at_non_Y:
                            operations += 1
            return operations
        
        min_operations = float('inf')
        for y_val in range(3):
            for non_y_val in range(3):
                if y_val != non_y_val:
                    min_operations = min(min_operations, calculate_operations(y_val, non_y_val))
        
        return min_operations