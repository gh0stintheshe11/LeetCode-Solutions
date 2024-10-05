# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_depth = self.get_depth(root, True)
        right_depth = self.get_depth(root, False)
        
        if left_depth == right_depth:
            return (1 << left_depth) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    def get_depth(self, node: Optional[TreeNode], is_left: bool) -> int:
        depth = 0
        while node:
            node = node.left if is_left else node.right
            depth += 1
        return depth