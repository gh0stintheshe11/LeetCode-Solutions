"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        if not root:
            return None
        
        binary_root = TreeNode(root.val)

        if root.children:
            binary_root.left = self.encode(root.children[0])

        current = binary_root.left
        for child in root.children[1:]:
            current.right = self.encode(child)
            current = current.right
        
        return binary_root

    # Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        if not data:
            return None

        n_ary_root = Node(data.val, [])

        binary_child = data.left
        while binary_child:
            n_ary_root.children.append(self.decode(binary_child))
            binary_child = binary_child.right
        
        return n_ary_root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))