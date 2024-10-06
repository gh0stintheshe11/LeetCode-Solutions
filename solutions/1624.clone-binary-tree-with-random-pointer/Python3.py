# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

# Definition for NodeCopy.
class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root:
            return None

        mapping = {}

        def clone(node):
            if not node:
                return None
            if node in mapping:
                return mapping[node]
            
            copy = NodeCopy(node.val)
            mapping[node] = copy
            
            copy.left = clone(node.left)
            copy.right = clone(node.right)
            copy.random = clone(node.random)
            
            return copy

        return clone(root)