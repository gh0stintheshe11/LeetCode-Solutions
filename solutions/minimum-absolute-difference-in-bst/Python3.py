# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder_traversal(node):
            if not node:
                return
            inorder_traversal(node.left)
            nodes.append(node.val)
            inorder_traversal(node.right)
        
        nodes = []
        inorder_traversal(root)
        min_diff = float('inf')
        for i in range(1, len(nodes)):
            min_diff = min(min_diff, nodes[i] - nodes[i - 1])
        return min_diff