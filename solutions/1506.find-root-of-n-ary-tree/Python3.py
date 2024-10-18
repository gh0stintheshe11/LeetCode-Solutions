"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        node_sum = 0
        child_sum = 0
        
        for node in tree:
            node_sum += node.val
            for child in node.children:
                child_sum += child.val
        
        root_val = node_sum - child_sum
        
        for node in tree:
            if node.val == root_val:
                return node