"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        stack, output = [root], []
        
        while stack:
            node = stack.pop()
            output.append(node.val)
            stack.extend(reversed(node.children))
        
        return output