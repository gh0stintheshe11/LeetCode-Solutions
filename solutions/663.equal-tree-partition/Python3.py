# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        def get_tree_sum(node):
            if not node:
                return 0
            return node.val + get_tree_sum(node.left) + get_tree_sum(node.right)
        
        total_sum = get_tree_sum(root)
        
        if total_sum % 2 != 0:
            return False
        
        target_sum = total_sum // 2
        
        found_subtree_sums = set()
        
        def can_find_target(node):
            if not node:
                return 0
            
            subtree_sum = node.val + can_find_target(node.left) + can_find_target(node.right)
            
            if node != root:
                found_subtree_sums.add(subtree_sum)
            
            return subtree_sum
        
        can_find_target(root)
        
        return target_sum in found_subtree_sums