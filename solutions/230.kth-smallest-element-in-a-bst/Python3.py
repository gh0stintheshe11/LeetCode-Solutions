# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def in_order_traversal(node):
            if node is None:
                return
            yield from in_order_traversal(node.left)
            yield node.val
            yield from in_order_traversal(node.right)
        
        gen = in_order_traversal(root)
        for _ in range(k):
            kth_smallest = next(gen)
        return kth_smallest