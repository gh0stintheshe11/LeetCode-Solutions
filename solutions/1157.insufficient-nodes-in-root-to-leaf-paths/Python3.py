# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def dfs(node, sum_so_far):
            if not node:
                return None
            
            sum_so_far += node.val

            if not node.left and not node.right:  # if it's a leaf
                return None if sum_so_far < limit else node
            
            node.left = dfs(node.left, sum_so_far)
            node.right = dfs(node.right, sum_so_far)
            
            if not node.left and not node.right:  # if both children are pruned
                return None

            return node

        return dfs(root, 0)