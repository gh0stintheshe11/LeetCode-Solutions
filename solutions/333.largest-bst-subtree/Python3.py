# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return (float('inf'), float('-inf'), 0, True)

            left_min, left_max, left_size, left_is_bst = helper(node.left)
            right_min, right_max, right_size, right_is_bst = helper(node.right)

            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                current_size = 1 + left_size + right_size
                return (min(left_min, node.val), max(right_max, node.val), current_size, True)
            else:
                return (float('-inf'), float('inf'), max(left_size, right_size), False)

        return helper(root)[2]