# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        if not root:
            return [None, None]
        
        if root.val <= target:
            left, right = self.splitBST(root.right, target)
            root.right = left
            return [root, right]
        else:
            left, right = self.splitBST(root.left, target)
            root.left = right
            return [left, root]