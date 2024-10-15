# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(node, cur_min, cur_max):
            if not node:
                return cur_max - cur_min

            cur_min = min(cur_min, node.val)
            cur_max = max(cur_max, node.val)

            left_diff = helper(node.left, cur_min, cur_max)
            right_diff = helper(node.right, cur_min, cur_max)

            return max(left_diff, right_diff)

        return helper(root, root.val, root.val)