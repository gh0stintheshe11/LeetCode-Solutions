"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        def clone(node: 'Node') -> 'Node':
            if node is None:
                return None
            cloned_node = Node(node.val)
            for child in node.children:
                cloned_child = clone(child)
                cloned_node.children.append(cloned_child)
            return cloned_node

        return clone(root)