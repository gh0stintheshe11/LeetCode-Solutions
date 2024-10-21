# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.nodes = []
        self.index = -1
        self._inorder_leftmost(root)

    def _inorder_leftmost(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self) -> bool:
        return self.index < len(self.nodes) - 1 or bool(self.stack)

    def next(self) -> int:
        if self.index < len(self.nodes) - 1:
            self.index += 1
        else:
            next_node = self.stack.pop()
            self.nodes.append(next_node.val)
            self.index += 1
            self._inorder_leftmost(next_node.right)
        
        return self.nodes[self.index]

    def hasPrev(self) -> bool:
        return self.index > 0

    def prev(self) -> int:
        if self.index > 0:
            self.index -= 1
        return self.nodes[self.index]