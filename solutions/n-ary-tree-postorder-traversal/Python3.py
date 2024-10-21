# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def traverse(node):
            if not node:
                return
            for child in node.children:
                traverse(child)
            result.append(node.val)
        
        result = []
        traverse(root)
        return result


# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            for child in node.children:
                stack.append(child)
        
        return result[::-1]  # Reverse the result to get the correct postorder
