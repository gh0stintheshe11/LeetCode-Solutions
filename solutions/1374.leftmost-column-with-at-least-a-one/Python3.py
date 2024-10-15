class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # Get the dimensions of the matrix
        rows, cols = binaryMatrix.dimensions()
        
        # Start from the top-right corner of the matrix
        row, col = 0, cols - 1
        
        # Track the leftmost column with a 1
        leftmost_col = -1
        
        # While we are within bounds of the matrix
        while row < rows and col >= 0:
            # If we find a 1, update the leftmost column and move left
            if binaryMatrix.get(row, col) == 1:
                leftmost_col = col
                col -= 1
            else:
                # If we find a 0, move down
                row += 1
        
        return leftmost_col