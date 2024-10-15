# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeQueries(self, root: TreeNode, queries: List[int]) -> List[int]:
        from collections import defaultdict

        # Store the height of each node's subtree
        def calculate_height(node):
            if not node:
                return -1
            left_height = calculate_height(node.left)
            right_height = calculate_height(node.right)
            height = 1 + max(left_height, right_height)
            subtree_heights[node.val] = height
            return height
        
        # Calculate height of each subtree
        subtree_heights = defaultdict(int)
        calculate_height(root)

        # Store the max height if each node is removed
        remove_effects = defaultdict(int)

        # Postorder traversal to compute height effect of removing each subtree
        def postorder(node, cur_height, max_level):
            if not node:
                return
            # Subtree height without current level (i.e., parent effect)
            remove_effects[node.val] = max_level
            left_height = 0 if not node.left else subtree_heights[node.left.val] + 1
            right_height = 0 if not node.right else subtree_heights[node.right.val] + 1

            if node.left:
                new_max = max(max_level, cur_height + right_height)
                postorder(node.left, cur_height + 1, new_max)
            if node.right:
                new_max = max(max_level, cur_height + left_height)
                postorder(node.right, cur_height + 1, new_max)
        
        # Trigger the postorder traversal
        postorder(root, 0, 0)

        # Get the answers for each query
        return [remove_effects[q] for q in queries]