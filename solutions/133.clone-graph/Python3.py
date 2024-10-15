# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        node_map = {}
        
        def clone(node):
            if node in node_map:
                return node_map[node]
            
            copy = Node(node.val)
            node_map[node] = copy
            copy.neighbors = [clone(neighbor) for neighbor in node.neighbors]
            return copy
        
        return clone(node)