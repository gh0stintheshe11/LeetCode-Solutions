class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize sets to keep track of seen numbers in rows, columns, and sub-boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue
                
                # Calculate the index for the 3x3 sub-box
                box_index = (r // 3) * 3 + (c // 3)
                
                # Check if the number is already seen in the current row, column, or sub-box
                if num in rows[r] or num in cols[c] or num in boxes[box_index]:
                    return False
                
                # Add the number to the respective sets
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)
        
        return True
