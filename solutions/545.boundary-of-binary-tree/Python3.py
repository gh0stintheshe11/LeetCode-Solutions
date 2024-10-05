# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        def is_leaf(node):
            return node is not None and node.left is None and node.right is None

        def add_left_boundary(node):
            while node:
                if not is_leaf(node):
                    boundary.append(node.val)
                if node.left:
                    node = node.left
                else:
                    node = node.right

        def add_leaves(node):
            if node is None:
                return
            if is_leaf(node):
                if node != root:  # Ensure root is not added twice if it's the only node
                    boundary.append(node.val)
            else:
                add_leaves(node.left)
                add_leaves(node.right)

        def add_right_boundary(node):
            stack = []
            while node:
                if not is_leaf(node):
                    stack.append(node.val)
                if node.right:
                    node = node.right
                else:
                    node = node.left
            while stack:
                boundary.append(stack.pop())
                
        boundary = [root.val]
        
        if root.left:
            add_left_boundary(root.left)
        add_leaves(root)
        if root.right:
            add_right_boundary(root.right)
        
        return boundary