# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def get_height(node):
            if not node:
                return -1
            return 1 + max(get_height(node.left), get_height(node.right))

        def fill_matrix(matrix, node, row, left, right):
            if not node:
                return
            mid = (left + right) // 2
            matrix[row][mid] = str(node.val)
            fill_matrix(matrix, node.left, row + 1, left, mid - 1)
            fill_matrix(matrix, node.right, row + 1, mid + 1, right)

        height = get_height(root)
        rows = height + 1
        cols = (1 << rows) - 1  # 2^rows - 1
        matrix = [["" for _ in range(cols)] for _ in range(rows)]

        fill_matrix(matrix, root, 0, 0, cols - 1)
        return matrix