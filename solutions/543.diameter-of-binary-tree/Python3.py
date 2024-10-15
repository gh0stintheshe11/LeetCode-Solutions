# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        
        def height(node):
            if not node:
                return 0
            # Recursively find the height of the left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)
            
            # Update the diameter if the path through the current node is larger
            self.diameter = max(self.diameter, left_height + right_height)
            
            # Return the height of the current node
            return 1 + max(left_height, right_height)
        
        height(root)
        return self.diameter
