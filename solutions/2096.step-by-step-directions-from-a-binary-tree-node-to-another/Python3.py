# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def find_path(node, value, path):
            if not node:
                return False
            if node.val == value:
                return True

            path.append('L')
            if find_path(node.left, value, path):
                return True
            path.pop()

            path.append('R')
            if find_path(node.right, value, path):
                return True
            path.pop()

            return False

        start_path, dest_path = [], []
        find_path(root, startValue, start_path)
        find_path(root, destValue, dest_path)

        i = 0
        while i < len(start_path) and i < len(dest_path) and start_path[i] == dest_path[i]:
            i += 1

        return 'U' * (len(start_path) - i) + ''.join(dest_path[i:])