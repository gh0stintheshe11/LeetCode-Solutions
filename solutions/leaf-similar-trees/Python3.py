# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeaves(node):
            leaves = []
            stack = [node]
            while stack:
                curr = stack.pop()
                if curr:
                    if not curr.left and not curr.right:
                        leaves.append(curr.val)
                    else:
                        stack.append(curr.right)
                        stack.append(curr.left)
            return leaves
        
        return getLeaves(root1) == getLeaves(root2)