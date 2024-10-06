# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        def build_balanced_tree(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = build_balanced_tree(nums[:mid])
            root.right = build_balanced_tree(nums[mid + 1:])
            return root

        sorted_vals = inorder(root)
        return build_balanced_tree(sorted_vals)