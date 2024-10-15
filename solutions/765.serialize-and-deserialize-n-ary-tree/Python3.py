"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ''
        
        result = []
        def dfs(node: 'Node'):
            if not node:
                return
            result.append(str(node.val))
            result.append(str(len(node.children)))
            for child in node.children:
                dfs(child)
        
        dfs(root)
        return ' '.join(result)
    
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        
        data = iter(data.split())
        
        def dfs() -> 'Node':
            val = int(next(data))
            size = int(next(data))
            node = Node(val, [])
            for _ in range(size):
                node.children.append(dfs())
            return node
        
        return dfs()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))