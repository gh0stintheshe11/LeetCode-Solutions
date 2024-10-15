# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        
        # Directions for right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0
        
        row, col = 0, 0
        
        current = head
        while current:
            matrix[row][col] = current.val
            current = current.next
            
            # Calculate next cell
            next_row = row + directions[dir_idx][0]
            next_col = col + directions[dir_idx][1]
            
            # Check if the next cell is within bounds and is unvisited
            if 0 <= next_row < m and 0 <= next_col < n and matrix[next_row][next_col] == -1:
                row, col = next_row, next_col
            else:
                # Change direction clockwise: right -> down -> left -> up
                dir_idx = (dir_idx + 1) % 4
                row += directions[dir_idx][0]
                col += directions[dir_idx][1]
        
        return matrix