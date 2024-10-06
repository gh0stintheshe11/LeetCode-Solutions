# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def diameter(self, root: 'Node') -> int:
        self.max_diameter = 0
        
        def dfs(node: 'Node') -> int:
            if not node.children:
                return 0
            
            max1, max2 = 0, 0
            for child in node.children:
                h = dfs(child) + 1
                if h > max1:
                    max1, max2 = h, max1
                elif h > max2:
                    max2 = h
            
            self.max_diameter = max(self.max_diameter, max1 + max2)
            return max1
        
        dfs(root)
        return self.max_diameter