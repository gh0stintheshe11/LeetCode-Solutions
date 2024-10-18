# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        self.left_count = 0
        self.right_count = 0
        
        def count_nodes(node: TreeNode) -> int:
            if not node:
                return 0
            left_subtree_count = count_nodes(node.left)
            right_subtree_count = count_nodes(node.right)
            if node.val == x:
                self.left_count = left_subtree_count
                self.right_count = right_subtree_count
            return 1 + left_subtree_count + right_subtree_count
        
        total_nodes = count_nodes(root)
        
        parent_count = n - (self.left_count + self.right_count + 1)
        
        player2_choice_max = max(self.left_count, self.right_count, parent_count)
        
        return player2_choice_max > n / 2