# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def is_unival(node: Optional[TreeNode], parent_val: int) -> bool:
            nonlocal count
            if node is None:
                return True
            
            left_check = is_unival(node.left, node.val)
            right_check = is_unival(node.right, node.val)
            
            if left_check and right_check:
                count += 1
                return node.val == parent_val
            
            return False
        
        count = 0
        is_unival(root, None)
        return count